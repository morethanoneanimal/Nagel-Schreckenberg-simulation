import unittest, functools
from simulation.car import Car
from simulation.road import Road
from simulation.speedLimits import *

class TestAvoidingCollisions(unittest.TestCase):
    def test_avoid_collisions(self):
        road = Road(5, 10, None)
        cars1 = [Car(road, (0, 0)), Car(road, (0, 2)), Car(road, (0, 4))]
        cars2 = [Car(road, (1, 0)), Car(road, (1, 3))]
        cars3 = [Car(road, (2, 3)), Car(road, (2, 4))]
        road.placeObjects( cars1 + cars2 + cars3 )
        for car in cars1:
            self.assertFalse( road.possibleLaneChangeUp(car.pos) )
            self.assertFalse( road.possibleLaneChangeDown(car.pos) )
        self.assertTrue( road.possibleLaneChangeDown(cars2[0].pos) )
        self.assertFalse( road.possibleLaneChangeUp(cars2[0].pos) )
        self.assertTrue( road.possibleLaneChangeDown(cars2[1].pos) )
        self.assertTrue( road.possibleLaneChangeUp(cars2[1].pos) )

        self.assertTrue( road.possibleLaneChangeUp(cars3[0].pos ))
        self.assertFalse( road.possibleLaneChangeDown(cars3[0].pos ))
        self.assertFalse( road.possibleLaneChangeUp(cars3[1].pos ))
        self.assertFalse( road.possibleLaneChangeDown(cars3[1].pos ))

class TestChangingLane(unittest.TestCase):
    def assertNotWillingToChange(self, car):
        self.assertFalse(car.willingToChangeUp())
        self.assertFalse(car.willingToChangeDown())

    def setUp(self):
        speedLimit1 = SpeedLimit( range=((50, 0), (80, 0)), limit=1, ticks=0)
        obstacle = SpeedLimit.createObstacle( (90, 0) )
        self.maxSpeed = 5
        self.oneLaneRoad = Road(1, 100, SpeedLimits( [speedLimit1], self.maxSpeed ))
        self.twoLaneRoad = Road(2, 100, SpeedLimits( [speedLimit1, obstacle], self.maxSpeed ))
        self.threeLaneRoad = Road(3, 100, SpeedLimits( [speedLimit1, obstacle], self.maxSpeed ))

    def test_one_lane(self):
        road = self.oneLaneRoad
        car = Car(road, (0, 0))
        road.placeObject(car)

        self.assertNotWillingToChange(car)

    def test_avoid_obstacle(self):
        road = self.twoLaneRoad
        car = Car(road, (89, 0), self.maxSpeed)
        road.placeObject(car)

        self.assertTrue( car.willingToChangeDown() )
        self.assertFalse( car.willingToChangeUp() )

    def test_change_for_speed(self):
        road = self.twoLaneRoad
        car = Car(road, (50, 0))
        road.placeObject(car)

        self.assertTrue( car.willingToChangeDown() )
        self.assertFalse( car.willingToChangeUp() )

    def test_free_rider(self):
        road = self.threeLaneRoad
        car = Car(road, (0, 1))
        road.placeObject(car)

        self.assertNotWillingToChange(car)

    def test_change_because_car_ahead(self):
        road = self.threeLaneRoad
        car1, car2 = Car(road, (0, 1), 5), Car(road, (2, 1), 5)
        road.placeObjects( [car1, car2] )

        self.assertTrue( car1.willingToChangeUp() and car1.willingToChangeDown() )
        self.assertNotWillingToChange(car2)

    def test_dont_change_because_car_is_near(self):
        road = self.threeLaneRoad
        carBlocked1, carBlocking1 = Car(road, (50, 0) ), Car(road, (50, 1))

        road.placeObjects( [carBlocked1, carBlocking1] )
        self.assertNotWillingToChange(carBlocked1)
        self.assertNotWillingToChange(carBlocking1)
