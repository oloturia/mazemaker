# mazemaker
a simple tool for drawing mazes in python

options
$ python3 -x <width> -y <height> -s <start Y> <start X> -e <exit Y> <exit X>

default values are 30x20 start 2 2 exit 17 27

The script returns a matrix of numbers, 0 is a full room, 1 an empty room and -1 the outer wall
also 2 is the starting point and 3 the exit

If launched as main, it prints the maze with ASCII blocks.
