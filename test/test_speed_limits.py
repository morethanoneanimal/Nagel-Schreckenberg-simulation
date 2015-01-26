import unittest
from simulation.speedLimits import *

class TestSpeedLimit(unittest.TestCase):
    def setUp(self):
        self.static = SpeedLimit( ((20, 0), (40, 3)), 3, 0, True)
        self.lights = SpeedLimit( ((120, 0), (120, 3)), 0, 20, True)
        self.obstacle = SpeedLimit( ((150, 0), (150, 0)), 0, 0, True)

    def assertInRange(self):
        self.assertTrue(self.static.inRange((20, 0)))
        self.assertTrue(self.static.inRange((40, 3)))
        self.assertTrue(self.static.inRange((29, 1)))
        self.assertFalse(self.static.inRange((0, 1)))
        self.assertFalse(self.static.inRange((41, 1)))
        self.assertFalse(self.static.inRange((19, 1)))

        self.assertTrue(self.lights.inRange( (120, 0) ))
        self.assertTrue(self.lights.inRange( (120, 3) ))
        self.assertFalse(self.lights.inRange( (119, 0) ))
        self.assertFalse(self.lights.inRange( (121, 0) ))

        self.assertTrue(self.obstacle.inRange( (150, 0) ) )
        self.assertFalse(self.obstacle.inRange( (150, 1) ) )

    def test_update(self):
        self.assertInRange()

        for x in range(21):
            self.static.update()
            self.lights.update()
            self.obstacle.update()

        self.assertFalse(self.lights.active)
        self.assertTrue(self.static.active or self.obstacle.active)
