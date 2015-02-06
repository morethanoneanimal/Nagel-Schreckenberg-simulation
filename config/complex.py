from simulation.speedLimits import *
from simulation.trafficGenerators import * 

maxFps= 40
size = width, heigth = 1280, 800
# in miliseconds
updateFrame = 500

lanes = 5
length = 190

maxSpeed = 5
maxLength = 1000

t = 50
l = 50
speedLimits = [
        SpeedLimit(range=((0, 2), (l, 2)), limit=0, ticks=0),
        SpeedLimit(range=((l, 0), (l, 1)), limit=0, ticks=t, active=False),
        SpeedLimit(range=((l, 3), (l, 4)), limit=0, ticks=t)
        ]
trafficGenerator = SimpleTrafficGenerator(1)
slowDownProbability, laneChangeProbability = 0.3, 0.2
