# NeighboringNodes
In my interpretation of this NeighboringNodes problem, the center node is a part of the neighborhood.

## prerequisites
Python3

## Running 
open command line

git checkout git@github.com:maymag/Neighboring-Nodes.git # clone the repo

cd neighboring-nodes # change directory into the project folder

python grid.py -h # passing -h will provide you available arguments to pass to the script

example command for grid.py:

python grid.py 8 2 1 'diamond' 2 -center 4 4 

('8' is grid size, '2' is index, '1' is debug, ''diamond'' is shape, '2' is radius, '-center 4 4' is for the x and y coordinates of the shape center)

example command for grid.py:

python grid.py 9 1 0 'cross' 3 -center_idx 33 

('9' is grid size, '1' is index, '0' is debug, ''cross'' is shape, '3' is radius, '-center_idx 33' is shape center index)

You must enter -center or -center_idx keyword arguments but you can't enter both.
