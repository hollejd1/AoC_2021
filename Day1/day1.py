import numpy as np
import math

fname = 'Day1/inp.txt'


input_array = np.genfromtxt(fname)

count_1 = 0
for i,val in enumerate(input_array[1:]):
    if val > input_array[i]:
        count_1 += 1

sum_array = np.zeros(input_array.shape[0]-2)

for i,val in enumerate(input_array[2:]):
    sum_array[i] = input_array[i:i+3].sum()

count_2 = 0
for i,val in enumerate(sum_array[1:]):
    if val > sum_array[i]:
        count_2 += 1

print('Part 1: {}'.format(count_1))
print('Part 2: {}'.format(count_2))