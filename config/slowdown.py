from simulation.speedLimits import *
from simulation.trafficGenerators import * 

maxFps= 40
size = width, heigth = 1280, 720
# in miliseconds
updateFrame = 500

seed = None

lanes = 3
length = 168*2

maxSpeed = 5
maxLength = 1000

speedLimits = [
        SpeedLimit(range=((70, 0), (130, lanes-1)), limit=3, ticks=0),
        SpeedLimit(range=((200, 0), (260, 0)), limit=2, ticks=0),
        SpeedLimit(range=((200, 2), (260, 2)), limit=2, ticks=0)
        ]
trafficGenerator = SimpleTrafficGenerator(2)
slowDownProbability, laneChangeProbability = 0.3, 0.2
