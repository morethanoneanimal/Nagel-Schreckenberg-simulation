import pygame

class InfoDisplayer():
    def __init__(self, screen, road, simulationManager):
        self.screen = screen
        self.road = road
        self.simulationManager = simulationManager
        self.string = ''
        self.cells = road.getCellCount()
        self.timeFactor = 0
        self.font = pygame.font.SysFont("monospace", 15)
        self.keysInfo = "Space - pause, M - 2x faster, N - 2x slower, S - step, D - 500 steps"
        self.text = [self.keysInfo]
        self.renderLabels()

    def renderLabels(self):
        self.labels = list(map(lambda x: self.font.render(x, 1, (255, 255, 0)), self.text))

    def update(self):
        totalCars, avgSpeed = self.road.getAvgCarSpeed()
        deadCars = self.road.deadCars
        updates = self.road.updates
        congestion = totalCars*100/self.cells

        text = [self.text[0]]
        text.append("avg speed: {:0.3f}".format(avgSpeed, deadCars))
        text.append("updates: " + str(updates))
        text.append("dead cars: " + str(deadCars))
        text.append("congestion: {:0.3f}".format(congestion))
        text.append('')
        text.append(self.keysInfo)
        self.text = text
        self.renderLabels()

    def updateSpeed(self):
        if len(self.text) == 0: return
        if self.timeFactor != self.simulationManager.timeFactor:
            self.timeFactor = self.simulationManager.timeFactor
            self.text[0] = "speed: {0}x".format(self.timeFactor)
            self.renderLabels()

    def draw(self):
        self.updateSpeed()
        y = self.screen.get_height() - 160
        for label in self.labels:
            self.screen.blit(label, (20, y))
            y += 20
