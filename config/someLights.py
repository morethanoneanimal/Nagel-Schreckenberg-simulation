from simulation.speedLimits import *
from simulation.trafficGenerators import * 

maxFps= 40
size = width, heigth = 1280, 800
# in miliseconds
updateFrame = 500

seed = None

lanes = 1
length = 1100

maxSpeed = 5
maxLength = 10000

speedLimits = [ SpeedLimit(range=((300,0),(300,1)), limit=0, ticks=70) ]
trafficGenerator = SimpleTrafficGenerator(1)
slowDownProbability, laneChangeProbability = 0.4, 0.2
