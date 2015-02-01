import sys, pygame, simulation.road, simulation.speedLimits, random
from simulation.car import Car
from representation import Representation
from simulationManager import SimulationManager
from simulation.trafficGenerators import *

if len(sys.argv) != 2:
    print("Usage: python pyTraffic.py module_with_config")
    exit()
random.seed(100)
pygame.init()

config = __import__(sys.argv[1])
screen = pygame.display.set_mode(config.size)

clock = pygame.time.Clock()

simulation.car.slowDownProbability = config.slowDownProbability
simulation.car.laneChangeProbability = config.laneChangeProbability
speedLimits = simulation.speedLimits.SpeedLimits(config.speedLimits, config.maxSpeed)
road = simulation.road.Road(config.lanes, config.length, speedLimits)
representation = Representation(screen, road, config.updateFrame)
simulation = SimulationManager(road, config.trafficGenerator, config.updateFrame)

while simulation.running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            simulation.processKey(event.key)
    clock.tick_busy_loop(config.maxFps)
    dt = clock.get_time()
    simulation.update(dt)
    representation.draw(dt * simulation.timeFactor)
    pygame.display.flip()

print("Goodbye")