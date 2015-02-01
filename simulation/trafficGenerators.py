import random

class SimpleTrafficGenerator():
    def __init__(self, carPerUpdate=1):
        self.queue = 0
        self.carPerUpdate = carPerUpdate
    def generate(self, road):
        amount = random.randint(0, self.carPerUpdate)
        self.tryGenerate(road, amount)

    def tryGenerate(self, road, amount):
        added = road.pushCarsRandomly(amount + self.queue)
        self.queue += (amount - added)


