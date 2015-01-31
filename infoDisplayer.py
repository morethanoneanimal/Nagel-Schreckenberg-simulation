import pygame

class InfoDisplayer():
    def __init__(self, screen, road):
        self.screen = screen
        self.road = road
        self.string = ''
        self.cells = road.getCellCount()
        self.font = pygame.font.SysFont("monospace", 15)
        self.labels = []

    def update(self):
        totalCars, avgSpeed = self.road.getAvgCarSpeed()
        deadCars = self.road.deadCars
        updates = self.road.updates
        congestion = totalCars*100/self.cells

        text = ["avg speed: {:0.3f}".format(avgSpeed, deadCars)]
        text.append("updates: " + str(updates))
        text.append("dead cars: " + str(deadCars))
        text.append("congestion: " + str(congestion))

        self.labels = list(map(lambda x: self.font.render(x, 1, (255, 255, 0)), text))
        #self.labels.append(self.font.render(self.string, 1, (255, 255, 0)))

    def draw(self):
        y = 500
        for label in self.labels:
            self.screen.blit(label, (20, y))
            y += 20
