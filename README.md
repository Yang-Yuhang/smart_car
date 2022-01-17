# smart_car
Bachelor course (Intelligent Engineer) project

## smartcar_description
The car model is built with a odometry,a hokuyo LiDAR and a camera, and the car is in a simply indoor environment. 

The python scripy can be used to control the movement of the car.

## smartcar_navigation
There are two functions in this package.

1. Mapping: use Gmapping algorithm to build up the map.

2. Navigation: use Adaptive Monte Carlo Localization (AMCL) algorithm to localize the car; use A* algorithm and Dynamic Window Approach (DWA) algorithm to do path planning and trajectory planning, separately.
