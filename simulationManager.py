import pygame

class SimulationManager:
    def __init__(self, road, trafficGenerator, updateFrame):
        self.road = road
        self.trafficGenerator = trafficGenerator
        self.updateFrame = updateFrame
        self.acc = 0
        self.timeFactor = 0.0
        self.prevTimeFactor = 1.0
        self.running = True
        self.stepsMade = 0

    def update(self, dt):
        self.acc += dt * self.timeFactor
        limit = 0
        if self.acc >= self.updateFrame:
            self.acc = self.acc % (self.updateFrame + 0)
            self.makeStep()

    def makeSteps(self, steps):
        for x in range(steps): self.makeStep()

    def makeStep(self):
        self.trafficGenerator.generate(self.road)
        self.road.update();
        self.stepsMade += 1

    def processKey(self, key):
        {
            pygame.K_ESCAPE: self.__exit,
            pygame.K_SPACE:  self.__pauseSwitch,
            pygame.K_m: self.__speedUp,
            pygame.K_n: self.__speedDown,
            pygame.K_s: self.__oneStepForward,
            pygame.K_d: self.__manyStepsForward(500)
        }.get(key, lambda: print("Unknown key"))()

    def isStopped(self):
        return self.timeFactor == 0

    def __exit(self): self.running = False
    def __pauseSwitch(self):
        self.timeFactor, self.prevTimeFactor = self.prevTimeFactor, self.timeFactor
    def __speedUp(self): self.timeFactor = min(8.0, self.timeFactor*2)
    def __speedDown(self): self.timeFactor = max(1/8, self.timeFactor/2)
    def __oneStepForward(self):
        if self.isStopped(): self.makeStep()
        else: print("Can't make step: simulation is running")
    def __manyStepsForward(self, steps):
        def manySteps():
            self.makeSteps(steps)
        return manySteps

