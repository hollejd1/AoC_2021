import numpy as np

fname = 'Day11/inp.txt'

input_array = np.genfromtxt(fname, dtype=str)
A = []
for i in range(input_array.shape[0]):
    row = []
    for j in range(len(input_array[i])):
        row.append(int(input_array[i][j]))
    A.append(row)
A = np.array(A, dtype=int)


ans_1 = 0
looping = True
n=0
all_flashed=False
while not all_flashed:
    A+=1
    flashed = []
    while np.argwhere(A>9).shape[0]>0:
        inds = np.argwhere(A>9)
        while inds.shape[0]>0:
            i = inds[0,0]
            j = inds[0,1]
            A[i,j]=-100
            for a in [-1,0,1]:
                for b in [-1,0,1]:
                    if i+a>=0 and i+a<10 and j+b>=0 and j+b<10:
                        A[i+a,j+b]+=1
            flashed.append(inds[0])
            inds = inds[1:]

    flashed = np.unique(flashed,axis=0)
    for ind in flashed:
        A[ind[0],ind[1]]=0
        if n<100:
            ans_1 +=1
    if flashed.shape[0]==100:
        all_flashed = True
        ans_2 = n+1
    n+=1

print('Part 1: {}'.format(ans_1))
print('Part 2: {}'.format(ans_2))