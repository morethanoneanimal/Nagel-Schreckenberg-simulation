import sys, pygame, config, simulation.road, random
from simulation.car import Car
from representation import Representation
from simulationManager import SimulationManager

random.seed(100)
pygame.init()

screen = pygame.display.set_mode(config.size)

clock = pygame.time.Clock()
acc = 0
#prevents update going into vicious circle
limit = 0

road = simulation.road.Road(config.lanes, config.length)
representation = Representation(screen, road)
simulation = SimulationManager(road)

while simulation.running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            simulation.processKey(event.key)
    clock.tick_busy_loop(config.maxFps)
    dt = clock.get_time()
    simulation.update(dt)
    if random.random() > 0.9:
        road.placeObject(Car(road, (0, int(random.random()*3))))
    representation.draw()
    pygame.display.flip()

print("Goodbye")
