import random, config

class Car:
    def __init__(self, road, pos):
        self.velocity = 1
        self.road = road
        self.pos = pos

    def update(self):
        self.velocity = self.velocity + 1
        self.velocity += 1
        # checking distance
        distance = self.road.distanceToNextThing(self.pos)
        self.velocity = min(self.velocity, distance, self.road.getSpeedLimitAt(self.pos))

        if self.velocity > 0 and random.random() >= 0.75:
            self.velocity -= 1

        self.pos = self.pos[0] + self.velocity, self.pos[1]
        return self.pos
