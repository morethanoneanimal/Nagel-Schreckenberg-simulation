import config, simulation.speedLimits
from functools import reduce
from simulation.car import Car

class Road:
    def __init__(self, lanesCount, length, speedLimits):
        self.lanes = []
        self.speedLimits = speedLimits if speedLimits != None else simulation.speedLimits.SpeedLimits([])
        for x in range(lanesCount):
            self.lanes.append( [None]*length )

    def update(self):
        self.speedLimits.update()
        for lane in self.lanes:
            for entity in lane:
                if entity != None:
                    entity.update()
        for lane in self.lanes:
            for entity in lane: 
                if entity != None:
                    entity.updated = False

    def addCar(self):
        if self.lanes[0][0] == None:
            self.lanes[0][0] = Car(self, (0,0))
            return True
        else:
            return False

    def carCount(self):
        return sum( reduce(lambda x, y: x+(0 if y == None else 1), lane, 0) for lane in self.lanes)

    def getMaxSpeedAtPos(self, pos):
        return self.speedLimits.getLimit(pos)

    def distanceToNextThing(self, pos):
        """Counts distance between given pos and next object (car or obstacle)"""
        return self.__distanceToNextThing((pos[0]+1, pos[1]))
    def __distanceToNextThing(self, pos):
        if pos[0] >= self.getLength():
            return self.getLength() # heaven
        else:
            if self.lanes[pos[1]][pos[0]] == None:
                return 1 + self.__distanceToNextThing((pos[0]+1, pos[1]))
            else:
                return 0

    def inBounds(self, pos):
        return pos[0] >= 0 and pos[1] >= 0 and pos[0] < self.getLength() and pos[1] < self.getLanesCount()

    def clearAt(self, pos):
        self.lanes[pos[1]][pos[0]] = None

    def placeObjects(self, entities):
        return all(self.placeObject(entity) for entity in entities)

    def placeObject(self, entity):
        if not self.inBounds(entity.pos): return False
        else:
            self.lanes[entity.pos[1]][entity.pos[0]] = entity
            return True

    def getLength(self):
        return len(self.lanes[0])
    def getLanesCount(self):
        return len(self.lanes)
