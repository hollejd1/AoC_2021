import numpy as np
from scipy import stats

fname = 'Day3/inp.txt'


input_array = np.genfromtxt(fname, dtype=str)

input_2D = []
for i in range(input_array.shape[0]):
    row = []
    for j in range(len(input_array[i])):
        row.append(input_array[i][j])
    input_2D.append(row)
input_2D = np.asarray(input_2D, dtype=int)

gamma = ''
epsilon = ''
a = stats.mode(input_2D, axis=0)[0][0]
for i in a:
    gamma += str(i)
    epsilon += str(int(i==0))

o2=np.arange(0,input_2D.shape[0])
Co2=np.arange(0,input_2D.shape[0])
for i in range(input_2D.shape[1]):
    if o2.shape[0]!=1:
        a = stats.mode(input_2D[o2,i], axis=0)[0][0]
        if stats.mode(input_2D[o2,i])[1][0]==o2.shape[0]//2:
            o2 = np.intersect1d(o2, np.argwhere(input_2D[:,i]==1))
        else:
            o2 = np.intersect1d(o2, np.argwhere(input_2D[:,i]==a))
    if Co2.shape[0]!=1:
        b = stats.mode(input_2D[Co2,i])[0][0]
        b = ~b + 2
        if stats.mode(input_2D[Co2,i])[1][0]==Co2.shape[0]//2:
            Co2 = np.intersect1d(Co2, np.argwhere(input_2D[:,i]==0))
        else:
            Co2 = np.intersect1d(Co2, np.argwhere(input_2D[:,i]==b))

o2_val = ''
Co2_val = ''
for i in range(input_2D.shape[1]):
    o2_val += str(input_2D[o2,i][0])
    Co2_val += str(input_2D[Co2,i][0])

ans_1 = int(gamma, base=2)*int(epsilon, base=2)
ans_2 = int(o2_val, base=2)*int(Co2_val, base=2)


print('Part 1: {}'.format(ans_1))
print('Part 2: {}'.format(ans_2))