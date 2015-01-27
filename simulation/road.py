import config, simulation.speedLimits
from functools import reduce
from simulation.car import Car

class Road:
    def __init__(self, lanesCount, length, speedLimits):
        self.lanes = Road.generateEmptyLanes(lanesCount, length)
        self.updatedLanes = Road.generateEmptyLanes(lanesCount, length)
        self.speedLimits = speedLimits if speedLimits != None else simulation.speedLimits.SpeedLimits([])

    def __updateCars(self, action):
        for lane in self.lanes:
            for entity in lane:
                if entity != None:
                    newPos = action(entity)
                    if self.inBounds(newPos):
                        self.updatedLanes[newPos[1]][newPos[0]] = entity
        self.flipLanes()

    def update(self):
        self.speedLimits.update()
        self.__updateCars(lambda x: x.updateLane())
        self.__updateCars(lambda x: x.updateX())

    def flipLanes(self):
        self.lanes = self.updatedLanes
        self.updatedLanes = Road.generateEmptyLanes(self.getLanesCount(), self.getLength())

    def addCar(self):
        if self.lanes[0][0] == None:
            self.lanes[0][0] = Car(self, (0,0))
            return True
        else:
            return False

    def pushCars(self, amount):
        total = 0
        for y in range(self.getLanesCount()):
            car = Car(self, (0, y), config.maxSpeed)
            if self.placeObject(car):
                total += 1
        return total


    def carCount(self):
        return sum( reduce(lambda x, y: x+(0 if y == None else 1), lane, 0) for lane in self.lanes)

    def getSpeedLimitAt(self, pos):
        return self.speedLimits.getLimit(pos)

    def distanceToNextThing(self, pos):
        """Counts distance between given pos and next object (car or obstacle), takes into considerations stops (speedLimit set to 0)"""
        return self.__distanceToNextThing((pos[0]+1, pos[1]))
    def __distanceToNextThing(self, pos):
        if pos[0] >= self.getLength():
            return self.getLength() # heaven
        else:
            if self.lanes[pos[1]][pos[0]] == None and not self.speedLimits.shouldStop(pos):
                return 1 + self.__distanceToNextThing((pos[0]+1, pos[1]))
            else:
                return 0

    def getMaxSpeedAt(self, pos):
        return min(self.getSpeedLimitAt(pos), self.distanceToNextThing(pos))

    def findPrevCar(self, pos):
        if not self.inBounds(pos) or self.getSpeedLimitAt(pos) == 0: return None
        else:
            if self.lanes[pos[1]][pos[0]] != None:
                return self.lanes[pos[1]][pos[0]]
            else:
                return self.findPrevCar( (pos[0] - 1, pos[1]) )

    def possibleLaneChangeUp(self, pos):
        return self.__possibleLaneChange(pos, pos[1]-1)
    def possibleLaneChangeDown(self, pos):
        return self.__possibleLaneChange(pos, pos[1]+1)
    def __possibleLaneChange(self, pos, destLane):
        if not self.inBounds( (0, destLane) ) or self.lanes[destLane][pos[0]] != None: return False
        else:
            sourceLane = pos[1]
            oneMoreLane = destLane + (destLane - sourceLane)
            if not self.inBounds( (0, oneMoreLane) ): return True
            else:
                return self.lanes[oneMoreLane][pos[0]] == None

    def inBounds(self, pos):
        return pos[0] >= 0 and pos[1] >= 0 and pos[0] < self.getLength() and pos[1] < self.getLanesCount()

    def clearAt(self, pos):
        self.lanes[pos[1]][pos[0]] = None

    def placeObjects(self, entities):
        return all(self.placeObject(entity) for entity in entities)

    def placeObject(self, entity):
        if not self.inBounds(entity.pos) or self.lanes[entity.pos[1]][entity.pos[0]] != None: return False
        else:
            self.lanes[entity.pos[1]][entity.pos[0]] = entity
            return True

    def getLength(self):
        return len(self.lanes[0])
    def getLanesCount(self):
        return len(self.lanes)

    def generateEmptyLanes(lanesCount, length):
        lanes = []
        for x in range(lanesCount):
            lanes.append( [None] * length )
        return lanes
