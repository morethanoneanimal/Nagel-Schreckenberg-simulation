import unittest, simulation.road, pygame
from simulationManager import *
from unittest.mock import Mock
from simulation.trafficGenerators import *

class TestSimulationManager(unittest.TestCase):
    def setUp(self):
        self.mock = Mock()
        self.trafficGeneratorMock = Mock()
        self.updateFrame = 500
        self.simulation = SimulationManager(self.mock, self.trafficGeneratorMock, self.updateFrame)

    def __setStopped(self, val):
        if self.simulation.isStopped() != val: self.simulation.processKey(pygame.K_SPACE)
        self.assertEqual(val, self.simulation.isStopped())

    def test_makeSteps(self):
        self.simulation.update(self.updateFrame)
        assert self.mock.update.called_once_with()
        assert self.trafficGeneratorMock.generate.called_once_with()

        x = 100
        self.simulation.makeSteps(x)
        self.assertEqual(x, self.mock.update.call_count)
        self.assertEqual(x, self.trafficGeneratorMock.generate.call_count)

    def test_space_key(self):
        self.assertTrue( self.simulation.isStopped() ) # default behaviour after init
        for x in range(100): self.simulation.update(self.updateFrame)
        self.assertEqual(0, self.mock.update.call_count)

        self.simulation.processKey(pygame.K_SPACE)
        self.assertFalse( self.simulation.isStopped() )
        self.assertEqual(1, self.simulation.timeFactor)
        for x in range(100): self.simulation.update(self.updateFrame)
        self.assertTrue(self.mock.update.call_count > 0)
        self.assertEqual(100, self.mock.update.call_count)

    def test_s_key(self):
        self.__setStopped(False)
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
