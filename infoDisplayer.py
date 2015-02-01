import pygame

class InfoDisplayer():
    def __init__(self, screen, road):
        self.screen = screen
        self.road = road
        self.string = ''
        self.cells = road.getCellCount()
        self.font = pygame.font.SysFont("monospace", 15)
        self.keysInfo = "Space = pause, M - 2x faster, N - 2x slower, S - step, D - 500 steps"
        self.renderLabels( [self.keysInfo] )

    def renderLabels(self, text):
        self.labels = list(map(lambda x: self.font.render(x, 1, (255, 255, 0)), text))

    def update(self):
        totalCars, avgSpeed = self.road.getAvgCarSpeed()
        deadCars = self.road.deadCars
        updates = self.road.updates
        congestion = totalCars*100/self.cells

        text = ["avg speed: {:0.3f}".format(avgSpeed, deadCars)]
        text.append("updates: " + str(updates))
        text.append("dead cars: " + str(deadCars))
        text.append("congestion: " + str(congestion))
        text.append('')
        text.append(self.keysInfo)
        self.renderLabels(text)

    def draw(self):
        y = self.screen.get_height() - 150
        for label in self.labels:
            self.screen.blit(label, (20, y))
            y += 20
