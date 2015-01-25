import random, config

class Car:
    def __init__(self, road, pos):
        self.velocity = 1
        self.road = road
        self.pos = pos
        self.updated = False

    def update(self):
        if self.updated: return
        self.velocity += 1
        # checking distance
        distance = self.road.distanceToNextThing(self.pos)
        self.velocity = min(self.velocity, distance, config.maxSpeed)

        if random.random() >= 0.75:
            self.velocity -= 1

        self.updated = True
        self.__move()

    def __move(self):
        self.road.clearAt(self.pos)
        self.pos = (self.pos[0]+self.velocity, self.pos[1])
        self.road.placeObject(self)
