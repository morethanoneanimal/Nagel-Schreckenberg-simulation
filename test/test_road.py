import unittest, functools
from simulation.road import Road
from simulation.car import Car
from simulation.speedLimits import *

class TestDistanceFunctions(unittest.TestCase):
    def setUp(self):
        speedLimits = SpeedLimits( [ SpeedLimit(range=((25, 0), (30, 0)), limit=1, ticks=0), SpeedLimit.createObstacle((80, 2)) ] , 5)
        self.road = Road(3, 100, speedLimits)
        self.freeCar = Car(self.road, (50, 0))
        self.carFacingObstacle = Car(self.road, (79, 2))
        self.car1 = Car(self.road, (75, 2))
        self.road.placeObjects([self.freeCar, self.carFacingObstacle, self.car1])

    def test_findPrevCar(self):
        length = self.road.getLength()
        for x in range(length):
            self.assertEqual(None, self.road.findPrevCar( (x, 1) ))
        for x in ((80, length)):
            self.assertEqual(None, self.road.findPrevCar( (x, 2) ))
        for x in range(50, length):
            self.assertEqual(self.freeCar, self.road.findPrevCar( (x, 0) ))
        self.assertEqual(self.car1, self.road.findPrevCar( (78, 2) ))

    def test_distanceToNextThing(self):
        for y in range(self.road.getLanesCount()):
            self.assertTrue( self.road.distanceToNextThing( (99, y)) >= self.road.getLength())

        self.assertEqual(0, self.road.distanceToNextThing( self.carFacingObstacle.pos ))
        self.assertEqual(3, self.road.distanceToNextThing( self.car1.pos ))
        self.assertEqual(49, self.road.distanceToNextThing( (0, 0) ) )

class TestRoad(unittest.TestCase):
    def setUp(self):
        self.maxSpeed = 5
        speedLimits = SpeedLimits( [ SpeedLimit(range=((25, 0), (30, 0)), limit=1, ticks=0), SpeedLimit.createObstacle((80, 2)) ], self.maxSpeed)
        self.road = Road(3, 100, speedLimits)

    def test_init(self):
        r = Road(3, 20, None)
        self.assertEqual(3, r.getLanesCount())
        self.assertEqual(20, r.getLength())
        self.assertEqual(r.carCount(), 0)

        # road is empty, so we should be able to add a car
        self.assertTrue(r.addCar())
        self.assertEqual(1, r.carCount())

    def test__getMaxSpeedAt(self):
        road = self.road
        self.assertEqual(self.maxSpeed, road.getMaxSpeedAt((0,0)))
        self.assertEqual(self.maxSpeed, road.getMaxSpeedAt((24,0)))
        self.assertEqual(self.maxSpeed, road.getMaxSpeedAt((31,0)))
        self.assertEqual(1, road.getMaxSpeedAt((25,0)))
        self.assertEqual(1, road.getMaxSpeedAt((26,0)))
        self.assertEqual(1, road.getMaxSpeedAt((30,0)))

    def test_inBounds(self):
        r = self.road
        self.assertFalse(r.inBounds((-1, -1)))
        self.assertFalse(r.inBounds((1, -1)))
        self.assertFalse(r.inBounds((-1, 2)))
        self.assertFalse(r.inBounds((100, 3)))
        self.assertTrue(r.inBounds((1, 1)))
        self.assertTrue(r.inBounds((0, 0)))
        self.assertTrue(r.inBounds((99, 2)))

    def test_placeObject(self):
        r = Road(3, 40, None)
        car1, car2 = Car(r, (20, 0)), Car(r, (30, 0))
        self.assertTrue(r.placeObjects([car1, car2]))
        self.assertEqual(2, r.carCount())
        self.assertEqual(9, r.distanceToNextThing(car1.pos))
        self.assertTrue(r.distanceToNextThing(car2.pos) >= r.getLength())
        car3 = Car(r, (21, 0))
        self.assertTrue( r.placeObject(car3) )
        self.assertEqual(3, r.carCount())
        self.assertEqual(0, r.distanceToNextThing(car1.pos))
        self.assertEqual(8, r.distanceToNextThing(car3.pos))

    def test_tunneling(self):
        # obstacle
        speedLimits = SpeedLimits( [SpeedLimit.createObstacle((10,0))], 5 )
        r = Road(1, 20, speedLimits)
        car = Car(r, (0,0))
        self.assertTrue(r.placeObject(car))
        for x in range(100):
            r.update()
        self.assertEqual(0, car.velocity)
        self.assertEqual((9, 0), car.pos)

    def test_pushCars(self):
         lanes = 5
         for x in range(lanes + 1):
             road = Road(lanes, 100, None)
             self.assertEqual(x, road.pushCars(x))
         for x in range(lanes + 1, 100):
             road = Road(lanes, 100, None)
             self.assertEqual(lanes, road.pushCars(x))

    def test_cant_push_car_on_stop(self):
         speedLimits = SpeedLimits( [SpeedLimit.createObstacle((0,1))], 5 )
         r = Road(3, 40, speedLimits)
         self.assertFalse( r.placeObject( Car(r, (0,1)) ))


