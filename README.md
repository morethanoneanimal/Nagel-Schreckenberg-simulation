# Nagel Schreckenberg simulation
Traffic simulation based on Nagel-Schreckenberg model with:
* n lanes,
* traffic lights,
* speed limits,
* obstacles.

[Youtube video](http://www.youtube.com/watch?v=9mvEJSlWZa8)

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/9mvEJSlWZa8/0.jpg)](http://www.youtube.com/watch?v=9mvEJSlWZa8)

In classic NS model cars move around in circle, so there is the same number of cars all the time. In this model they are generated in each iteration and once they reach the end of the road they are destroyed.

## How to run?
You need Python3 and Pygame installed. To run simulation: 
```
python nagel.py config.someLights
```

## How to create simulation?
Copy existing simulation in ```config``` directory, read comments in sample configs and play.
## Lane change model
In each iteration

1. Car checks maximum speed it can achieve on it's current position (x, lane) and adjacent lane (x, lane+1).
2. If the potential maximal speed on lane+1 is higher it checks safe conditions:
  1. There is no car car on (x, lane+2) to avoid collision caused by two parallel cars changing lane to lane+1.
  2. Distance to previous car on lane+1 is greater that it's speed to avoid emergency braking of previous car.
3. Change lane with probability P.

Same steps for lane-1
