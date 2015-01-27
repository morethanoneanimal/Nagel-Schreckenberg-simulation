import unittest, functools
from simulation.car import Car
from simulation.road import Road
from simulation.speedLimits import *

class TestAvoidingCollisions(unittest.TestCase):
    def test_avoid_collisions(self):
        road = Road(5, 10, None)
        cars1 = [Car(road, (0, 0)), Car(road, (0, 2)), Car(road, (0, 4))]
        cars2 = [Car(road, (1, 0)), Car(road, (1, 3))]
        road.placeObjects( cars1 + cars2 )
        for car in cars1:
            self.assertFalse( road.possibleLaneChangeUp(car.pos) )
            self.assertFalse( road.possibleLaneChangeDown(car.pos) )
        self.assertTrue( road.possibleLaneChangeDown(cars2[0].pos) )
        self.assertFalse( road.possibleLaneChangeUp(cars2[0].pos) )
        self.assertTrue( road.possibleLaneChangeDown(cars2[1].pos) )
        self.assertTrue( road.possibleLaneChangeUp(cars2[1].pos) )

