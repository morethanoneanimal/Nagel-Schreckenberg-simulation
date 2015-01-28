import pygame

class SimulationManager:
    def __init__(self, road, trafficGenerator, updateFrame):
        self.road = road
        self.trafficGenerator = trafficGenerator
        self.updateFrame = updateFrame
        self.acc = 0
        self.timeFactor = 0
        self.prevTimeFactor = 1
        self.running = True

    def update(self, dt):
        self.acc += dt * self.timeFactor
        limit = 0
        while self.acc >= self.updateFrame and limit < 10:
            self.acc -= self.updateFrame
            limit += 1
            self.makeStep()

    def makeSteps(self, steps):
        for x in range(steps): self.makeStep()

    def makeStep(self):
        self.trafficGenerator.generate(self.road)
        self.road.update();

    def processKey(self, key):
        {
                pygame.K_ESCAPE: self.__exit,
                pygame.K_SPACE:  self.__pauseSwitch,
                pygame.K_m: self.__speedUp,
                pygame.K_n: self.__speedDown,
                pygame.K_s: self.__oneStepForward
        }[key]()

    def isStopped(self):
        return self.timeFactor == 0

    def __exit(self): self.running = False
    def __pauseSwitch(self):
        self.timeFactor, self.prevTimeFactor = self.prevTimeFactor, self.timeFactor
    def __speedUp(self): self.timeFactor = min(8, self.timeFactor*2)
    def __speedDown(self): self.timeFactor = max(1/8, self.timeFactor/2)
    def __oneStepForward(self):
        if self.isStopped(): self.makeStep()
        else: print("Can't make step: simulation is running")

