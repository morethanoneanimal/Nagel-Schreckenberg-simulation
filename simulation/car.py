import random, config

class Car:
    def __init__(self, road, pos):
        self.velocity = 1
        self.road = road
        self.pos = pos

    def update(self):
        self.velocity = self.calcNewVelocity()

        if self.velocity > 0 and random.random() >= 0.75:
            self.velocity -= 1

        self.pos = self.pos[0] + self.velocity, self.pos[1]
        return self.pos

    def calcNewVelocity(self):
        return min(self.velocity + 1, self.road.getMaxSpeedAt(self.pos))
