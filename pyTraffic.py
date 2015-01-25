import sys, pygame, config, simulation.road, random
from simulation.car import Car
from representation import Representation

random.seed(100)
pygame.init()

screen = pygame.display.set_mode(config.size)
running = True

clock = pygame.time.Clock()
acc = 0
#prevents update going into vicious circle
limit = 0

road = simulation.road.Road(config.lanes, config.length)
representation = Representation(screen, road)

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    clock.tick_busy_loop(config.maxFps)
    dt = clock.get_time()
    acc += dt
    while acc >= config.updateFrame and limit < 10:
        acc -= config.updateFrame
        limit += 1
        road.update()
    limit = 0
    if random.random() > 0.9:
        road.placeObject(Car(road, (0, int(random.random()*3))))
    representation.draw()
    pygame.display.flip()

print("Goodbye")
