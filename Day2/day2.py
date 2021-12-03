import numpy as np
import math

fname = 'Day2/inp.txt'


input_array = np.genfromtxt(fname, dtype=str)
direction = input_array[:,0]
distance = input_array[:,1].astype('int')

movement = 0
depth = 0
aim = 0
for i,direct in enumerate(direction):
    if len(direct)==4:
        depth += distance[i]
        aim += distance[i]
    if len(direct)==2:
        depth -= distance[i]
        aim -= distance[i]
    if len(direct)==7:
        movement += distance[i]

ans_1 = depth*movement

movement = 0
depth = 0
aim = 0
for i,direct in enumerate(direction):
    if len(direct)==4:
        aim += distance[i]
    if len(direct)==2:
        aim -= distance[i]
    if len(direct)==7:
        movement += distance[i]
        depth += aim*distance[i]


ans_2 = movement*depth

print('Part 1: {}'.format(ans_1))
print('Part 2: {}'.format(ans_2))