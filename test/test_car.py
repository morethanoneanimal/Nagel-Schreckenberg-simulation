import unittest, random
from simulation.road import Road
from simulation.car import Car
from simulation.speedLimits import *

class TestCar(unittest.TestCase):
    def setUp(self):
        random.seed(None)
        self.maxSpeed = 5
        speedLimits = SpeedLimits( [ SpeedLimit(range=((50, 0), (99, 0)), limit=2, ticks=0) ], self.maxSpeed )
        road = self.road = Road(1, 100, speedLimits)
        self.car1 = Car(road, (0, 0))
        self.carA = Car(road, (25, 0))
        self.carB = Car(road, (26, 0))
        self.carC = Car(road, (28, 0))
        self.car2 = Car(road, (50, 0))
        self.allCars = [self.car1, self.carA, self.carB, self.carC, self.car2]
        self.road.placeObjects( self.allCars )

    def test_assumptions(self):
        for car in self.allCars:
            car.velocity = random.randint(-100, 100)
            newVelocity = car.calcNewVelocity()
            self.assertTrue( newVelocity <= self.road.distanceToNextThing(car.pos) )
            self.assertTrue( newVelocity <= self.road.getSpeedLimitAt(car.pos) )
            self.assertTrue( newVelocity <= self.maxSpeed)

