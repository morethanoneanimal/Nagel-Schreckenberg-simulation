import random, config

class Car:
    def __init__(self, road, pos, velocity = 0):
        self.velocity = velocity
        self.road = road
        self.pos = pos

    def updateLane(self):
        if self.willingToChangeUp():
            if random.random() >= 0.5:
                self.pos = self.pos[0], self.pos[1]-1
        elif self.willingToChangeDown():
            if random.random() >= 0.5:
                self.pos = self.pos[0], self.pos[1]+1
        return self.pos

    def updateX(self):
        self.velocity = self.calcNewVelocity()

        if self.velocity > 0 and random.random() >= 0.75:
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
            return distanceToPrevCar >= prevCar.velocity
