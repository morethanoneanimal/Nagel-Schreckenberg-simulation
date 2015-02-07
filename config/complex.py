from simulation.speedLimits import *
from simulation.trafficGenerators import *

maxFps= 40
#size of the window
size = width, heigth = 1280, 720
# in miliseconds
updateFrame = 500

# seed for pseudo random generator
seed = None

lanes = 5
# lenght of the road
length = 168

maxSpeed = 5

t = 50
l = 50
# speedLimits is the place where we can define traffic lights, obstacles and, of course, speed limits
# range is defined by two points that forms rectangle.
# limit - speed limit. If is set to 0 no car will enter it.
# ticks - time of activity. For example if 'ticks' are set to 10 then speed limit will be active for 10 iterations, then inactive for 10 and then active for 10 and so on and so on ..
# it ticks are set to 0 speed limit is active forever
# active - is speed limit active from the first iteration or not. Beware - if ticks are set to 0 and 'active' to False it'll be useless
speedLimits = [
        SpeedLimit(range=((0, 2), (l, 2)), limit=0, ticks=0), # this is the barrier between two roads at the beginning.
        SpeedLimit(range=((l, 0), (l, 1)), limit=0, ticks=t, active=False), # top lights
        SpeedLimit(range=((l, 3), (l, 4)), limit=0, ticks=t) # bottom lights
        ]

# traffic generator that is responsible for generating cars each iteration. 
trafficGenerator = SimpleTrafficGenerator(2) # this generator at each iteration will generate random(0, 2) cars
slowDownProbability, laneChangeProbability = 0.3, 0.5 # slowDownProbability - from NaSch model. laneChangeProbability - from my model
