import random

class SimpleTrafficGenerator():
    def __init__(self):
        self.queue = 0
    def generate(self, road):
        amount = random.randint(0, 2)
        self.tryGenerate(road, amount)

    def tryGenerate(self, road, amount):
        added = road.pushCarsRandomly(amount + self.queue)
        self.queue += (amount - added)


