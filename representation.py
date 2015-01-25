import pygame, config

class Representation():
    def __init__(self, screen, road):
        self.screen = screen
        self.road = road
        self.margins = (10, 10)
        self.cellSize = 10

    def draw(self):
        self.screen.fill( (0, 100, 100) )
        self.drawRoad()

    def drawRoad(self):
        y = self.margins[1]
        for lane in self.road.lanes:
            self.__drawLane(lane, y)
            y += self.cellSize

    def __drawLane(self, lane, y):
        x = self.margins[0]
        for cell in lane:
            if cell != None:
                pygame.draw.rect(self.screen, (200,200,0), (x,y,self.cellSize,self.cellSize), 0)
            pygame.draw.rect(self.screen, (0, 230, 0), (x,  y, self.cellSize, self.cellSize), 2)

            x += self.cellSize
            if x + self.cellSize + self.margins[0] >= config.width:
                x = self.margins[0]
                y += 50
