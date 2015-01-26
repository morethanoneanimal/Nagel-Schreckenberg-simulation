import config

class SpeedLimits:
    def __init__(self, listOfTuples):
        self.speedLimits = list(map(lambda x: SpeedLimit(x[0], x[1], x[2], x[3]), listOfTuples))

    def update(self):
        for speedLimit in self.speedLimits:
            speedLimit.update()

    def getLimit(self, pos):
        for speedLimit in self.speedLimits:
            if speedLimit.active and speedLimit.inRange(pos):
                return speedLimit.speedLimit
        # limit not found, returnig max speed
        return config.maxSpeed

    def shouldStop(self, pos):
        return self.getLimit(pos) == 0

class SpeedLimit:
    def __init__(self, range, speedLimit, ticks, active):
        self.lanes = (range[0][1], range[1][1])
        self.xPos = (range[0][0], range[1][0])
        self.speedLimit = speedLimit
        self.ticks = ticks
        self.active = active
        self.acc = 0

    def inRange(self, pos):
        return (self.lanes[0] <= pos[1] <= self.lanes[1]) and (self.xPos[0] <= pos[0] <= self.xPos[1])

    def update(self):
        if self.ticks > 0:
            self.acc += 1
            if self.acc >= self.ticks:
                self.acc = 0
                self.active = not self.active

