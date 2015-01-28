import pygame, config

class Representation():
    def __init__(self, screen, road, updateFrame):
        self.screen = screen
        self.road = road
        self.updateFrame = updateFrame
        self.margins = (10, 10)
        self.cellSize = 15
        self.acc = 0

        self.colors = [ (255, 0, 0), (180, 20, 0), (80, 60, 0), (100, 80, 0), (0, 180, 0), (0, 255, 0), (80, 120, 0), (60, 140, 0), (40, 160, 0) ]

    def draw(self, dt):
        self.__updateAcc(dt)
        self.screen.fill( (0, 0, 0) )
        self.drawRoad(dt)

    def drawRoad(self, dt):
        y = self.margins[1]
        for lane in self.road.lanes:
            self.__drawLane(lane, y, dt)
            y += self.cellSize

    def __drawLane(self, lane, y, dt):
        x = self.margins[0]
        for cell in lane:
            pygame.draw.rect(self.screen, (0, 30, 200), (x,  y, self.cellSize, self.cellSize), 2)
            if cell != None:
                self.__drawCar(cell, x, y)

            x += self.cellSize
            if x + self.cellSize + self.margins[0] >= config.width:
                x = self.margins[0]
                y += (self.road.getLanesCount() + 1)  * self.cellSize

    def __drawCar(self, car, x, y):
        invProgress = (1 - self.acc / self.updateFrame)*self.cellSize
        offset = (car.prevPos[0] - car.pos[0])*invProgress, (car.prevPos[1] - car.pos[1])*invProgress
        pygame.draw.rect(self.screen, self.colors[car.velocity], (x+offset[0],y+offset[1],self.cellSize,self.cellSize), 0)

    def __updateAcc(self, dt):
        self.acc += dt
        self.acc = self.acc % (self.updateFrame + 0)
