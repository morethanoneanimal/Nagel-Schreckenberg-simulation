from simulation.speedLimits import *
from simulation.trafficGenerators import * 

maxFps= 40
size = width, heigth = 1480, 480
# in miliseconds
updateFrame = 500

lanes = 5
length = 200

maxSpeed = 5
maxLength = 10000

speedLimits = [SpeedLimit( range=((100,1),(100,1)), limit=0, ticks=200, active=False)]
trafficGenerator = SimpleTrafficGenerator()
