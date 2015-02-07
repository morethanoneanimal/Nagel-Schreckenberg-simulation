import random

class Car:
    slowDownProbability = 0
    laneChangeProbability = 0
    def __init__(self, road, pos, velocity = 0):
        self.velocity = velocity
        self.road = road
        self.pos = pos
        self.prevPos = pos

    def updateLane(self):
        self.prevPos = self.pos
        if self.willingToChangeUp():
            if random.random() >= Car.laneChangeProbability:
                self.pos = self.pos[0], self.pos[1]-1
        elif self.willingToChangeDown():
            if random.random() >= Car.laneChangeProbability:
                self.pos = self.pos[0], self.pos[1]+1
        return self.pos

    def updateX(self):
        self.velocity = self.calcNewVelocity()

        if self.velocity > 0 and random.random() <= Car.slowDownProbability:
            self.velocity -= 1

        self.pos = self.pos[0] + self.velocity, self.pos[1]
        return self.pos

    def calcNewVelocity(self):
        return min(self.velocity + 1, self.road.getMaxSpeedAt(self.pos))

    def willingToChangeUp(self):
        return self.road.possibleLaneChangeUp(self.pos) and self.__willingToChangeLane(self.pos[1], self.pos[1] - 1)
    def willingToChangeDown(self):
        return self.road.possibleLaneChangeDown(self.pos) and self.__willingToChangeLane(self.pos[1], self.pos[1] + 1)

    def __willingToChangeLane(self, sourceLane, destLane):
        srcLaneSpeed = self.road.getMaxSpeedAt( (self.pos[0], sourceLane) )
        destLaneSpeed = self.road.getMaxSpeedAt( (self.pos[0], destLane) )
        if destLaneSpeed <= srcLaneSpeed: return False
        prevCar = self.road.findPrevCar( (self.pos[0], destLane) )
        if prevCar == None: return True
        else:
            distanceToPrevCar = self.pos[0] - prevCar.pos[0]
            return distanceToPrevCar > prevCar.velocity
