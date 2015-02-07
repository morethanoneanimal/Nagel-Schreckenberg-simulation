from simulation.speedLimits import *
from simulation.trafficGenerators import * 

maxFps= 40
size = width, heigth = 1280, 800
# in miliseconds
updateFrame = 500

seed = None

lanes = 15
length = 190

maxSpeed = 5
maxLength = 1000

speedLimits = [ SpeedLimit(range=((50, 6), (100,6)), limit=0, ticks=0)]
trafficGenerator = SimpleTrafficGenerator(10)
slowDownProbability, laneChangeProbability = 0.3, 0.2
