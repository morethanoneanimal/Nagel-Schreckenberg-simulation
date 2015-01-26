import unittest, config, simulation.road, pygame
from simulationManager import *
from unittest.mock import Mock

class TestSimulationManager(unittest.TestCase):
    def setUp(self):
        self.mock = Mock()
        self.simulation = SimulationManager(self.mock)

    def test_makeSteps(self):
        #mock = simulation.road.Road(3, 100)
        mock = Mock()
        s = SimulationManager(mock)
        assert mock.update.called_once_with()

        x = 100
        s.makeSteps(x)
        self.assertEqual(x, mock.update.call_count)
    def test_space_key(self):
        self.assertTrue( self.simulation.isStopped() ) # default behaviour after init
        for x in range(100): self.simulation.update(config.updateFrame)
        self.assertEqual(0, self.mock.update.call_count)

        self.simulation.processKey(pygame.K_SPACE)
        self.assertFalse( self.simulation.isStopped() )
        self.assertEqual(1, self.simulation.timeFactor)
        for x in range(100): self.simulation.update(config.updateFrame)
        self.assertTrue(self.mock.update.call_count > 0)
        self.assertEqual(100, self.mock.update.call_count)

    def test_escape_key(self):
        self.simulation.processKey(pygame.K_ESCAPE)
        self.assertFalse(self.simulation.running)
