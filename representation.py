import pygame
from infoDisplayer import *

class Representation():
    def __init__(self, screen, road, simulationManager):
        self.screen = screen
        self.width, self.heigth = screen.get_width(), screen.get_height()
        self.road = road
        self.updateFrame = simulationManager.updateFrame
        self.margins = (10, 10)
        self.cellSize = 15
        self.acc = 0

        self.infoDisplayer = InfoDisplayer(screen, road, simulationManager)

        self.colors = [ (255, 0, 0), (180, 20, 0), (80, 60, 0), (100, 80, 0), (0, 180, 0), (0, 255, 0), (80, 120, 0), (60, 140, 0), (40, 160, 0) ]

    def draw(self, dt):
        self.__updateAcc(dt)
        self.screen.fill( (0, 0, 0) )
        self.drawRoad(dt)
        self.infoDisplayer.draw()

    def drawRoad(self, dt):
        y = 0
        for lane in self.road.lanes:
            self.__drawLane(lane, y, dt)
            y += self.cellSize

    def __drawLane(self, lane, y, dt):
        x = 0
        for cell in lane:
            idx = x / self.cellSize, y / self.cellSize
            speedLimit = self.road.getSpeedLimitAt(idx)
            self.__drawCell(x, y, speedLimit)
            if cell != None:
                self.__drawCar(cell, x, y)

            x += self.cellSize

    def __drawCell(self, x, y, speedLimit):
        realPos = self.__getPosOnScreen((x,y))
        factor = 30 + speedLimit*30
        pygame.draw.rect(self.screen, (factor, factor, factor), (realPos[0], realPos[1], self.cellSize, self.cellSize), 0)
#        pygame.draw.rect(self.screen, (0, 30, 200), (realPos[0], realPos[1], self.cellSize, self.cellSize), 2)

    def __drawCar(self, car, x, y):
        invProgress = (1 - self.acc / self.updateFrame)*self.cellSize
        offset = (car.prevPos[0] - car.pos[0])*invProgress, (car.prevPos[1] - car.pos[1])*invProgress
        realPos = self.__getPosOnScreen((x+offset[0], y+offset[1]))
        pygame.draw.rect(self.screen, self.colors[car.velocity], (realPos[0],realPos[1],self.cellSize,self.cellSize), 0)

    def __updateAcc(self, dt):
        self.acc += dt
        if self.acc >= self.updateFrame:
            self.infoDisplayer.update()
        self.acc = self.acc % (self.updateFrame + 0)

    def __getPosOnScreen(self, pos):
        x, y = pos
        while x + self.margins[0] >= self.width - self.margins[0]:
            x -= (self.width - 2*self.margins[0])
            y += (self.road.getLanesCount() + 1) * self.cellSize + self.cellSize
        return (x + self.margins[0], y + self.margins[1])
