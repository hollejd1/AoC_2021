import numpy as np

fname = 'Day6/inp.txt'

input_array = np.genfromtxt(fname, dtype=int,delimiter=',')

days = 80
fish = input_array.copy()
for i in range(days):
    fish -= 1
    new = np.argwhere(fish==-1).shape[0]
    fish[np.argwhere(fish==-1)] = 6
    fish = np.concatenate((fish, np.ones(new)*8))
ans_1=fish.shape[0]


days = 256
fish = np.zeros(9)
at_zero = 0
for i in range(9):
    fish[i] = (input_array==i).sum()
for i in range(days):
    at_zero = fish[0]
    fish[0:8] = fish[1:9]
    fish[6] += at_zero
    fish[8] = at_zero
ans_2=int(fish.sum())

print('Part 1: {}'.format(ans_1))
print('Part 2: {}'.format(ans_2))