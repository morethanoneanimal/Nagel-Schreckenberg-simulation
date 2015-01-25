import unittest, functools
import simulation.road, config
from simulation.car import Car

class TestRoad(unittest.TestCase):
    def setUp(self):
        self.road = simulation.road.Road(3, 100)

    def test_init(self):
        r = simulation.road.Road(3, 20)
        self.assertEqual(3, r.getLanesCount())
        self.assertEqual(20, r.getLength())
        self.assertEqual(r.carCount(), 0)

        # road is empty, so we should be able to add a car
        self.assertTrue(r.addCar())
        self.assertEqual(1, r.carCount())

    def test_inBounds(self):
        r = simulation.road.Road(3, 100)
        self.assertFalse(r.inBounds((-1, -1)))
        self.assertFalse(r.inBounds((1, -1)))
        self.assertFalse(r.inBounds((-1, 2)))
        self.assertFalse(r.inBounds((100, 3)))
        self.assertTrue(r.inBounds((1, 1)))
        self.assertTrue(r.inBounds((0, 0)))
        self.assertTrue(r.inBounds((99, 2)))

    def test_placeObject(self):
        r = simulation.road.Road(3, 40)
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
