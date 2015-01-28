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

speedLimits = simulation.speedLimits.SpeedLimits([simulation.speedLimits.SpeedLimit( range=((100,1),(100,1)), limit=0, ticks=200, active=False)], config.maxSpeed)
#speedLimits = simulation.speedLimits.SpeedLimits( [] )
road = simulation.road.Road(config.lanes, config.length, speedLimits)
representation = Representation(screen, road)
simulation = SimulationManager(road, SimpleTrafficGenerator())

while simulation.running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            simulation.processKey(event.key)
    clock.tick_busy_loop(config.maxFps)
    dt = clock.get_time()
    simulation.update(dt)
    representation.draw()
    pygame.display.flip()

print("Goodbye")
