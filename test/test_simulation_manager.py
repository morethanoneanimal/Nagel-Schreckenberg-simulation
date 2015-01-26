import unittest, config, simulation.road, pygame
from simulationManager import *
from unittest.mock import Mock

class TestSimulationManager(unittest.TestCase):
    def setUp(self):
        self.mock = Mock()
        self.simulation = SimulationManager(self.mock)

    def __setStopped(self, val):
        if self.simulation.isStopped() != val: self.simulation.processKey(pygame.K_SPACE)
        self.assertEqual(val, self.simulation.isStopped())

    def test_makeSteps(self):
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

    def test_s_key(self):
        self.__setStopped(False)
        self.mock.reset_mock()
        self.simulation.processKey(pygame.K_n)
        self.assertEqual(0, self.mock.update.call_count )
        self.simulation.processKey(pygame.K_SPACE)
        self.simulation.processKey(pygame.K_n)
        self.assertTrue( self.mock.update.called_once_with() )

    def test_n_key(self):
        """slowing down"""
        self.__setStopped(False)
        for x in range(20): self.simulation.processKey(pygame.K_n)
        self.assertEqual(1/8, self.simulation.timeFactor)

    def test_escape_key(self):
        self.simulation.processKey(pygame.K_ESCAPE)
        self.assertFalse(self.simulation.running)
