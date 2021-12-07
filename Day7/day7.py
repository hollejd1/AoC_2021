import numpy as np
from statistics import median
fname = 'Day7/inp_test.txt'

input_array = np.genfromtxt(fname, dtype=int,delimiter=',')

def tri(num):
    val = 0
    return np.arange(num+1).sum()

f = np.vectorize(tri)

cost_1 = np.arange(input_array.max())
cost_2 = np.arange(input_array.max())
for i in range(input_array.max()):
    cost_1[i] = (abs(input_array-i)).sum()
    cost_2[i] = (f(abs(input_array-i))).sum()

ans_1=np.min(cost_1)
ans_2=np.min(cost_2)
print('Part 1: {}'.format(ans_1),abs(input_array-round(median(input_array))).sum())
print('Part 2: {}'.format(ans_2),f(abs(input_array-round(input_array.mean()))).sum())