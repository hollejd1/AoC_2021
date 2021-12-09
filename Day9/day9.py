import numpy as np

fname = 'Day9/inp.txt'

input_array = np.genfromtxt(fname, dtype=str, delimiter='')

A = []
for i in range(input_array.shape[0]):
    row = []
    for j in range(len(input_array[0])):
        row.append(input_array[i][j])
    A.append(row)
A = np.array(A,dtype=int)

def is_min(A,i,j):
    localMin=True
    inds = [[-1,0],
            [0,-1],
            [1,0],
            [0,1]]
    if i==0:
        inds.remove([-1,0])
    elif i==A.shape[0]-1:
        inds.remove([1,0])

    if j==0:
        inds.remove([0,-1])
    elif j==A.shape[1]-1:
        inds.remove([0,1])
    
    for ind in inds:
        if A[i,j]>=A[i+ind[0],j+ind[1]]:
            localMin=False
    return localMin


ans_1 = 0

for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        if is_min(A,i,j):
            ans_1+= A[i,j] + 1

def get_surround(B,i,j,q_x,q_y):
    ones=0
    inds = [[-1,0],
            [0,-1],
            [1,0],
            [0,1]]
    if i==0:
        inds.remove([-1,0])
    elif i==A.shape[0]-1:
        inds.remove([1,0])

    if j==0:
        inds.remove([0,-1])
    elif j==A.shape[1]-1:
        inds.remove([0,1])
    
    for ind in inds:
        if B[i+ind[0],j+ind[1]]==1:
            q_x.append(i+ind[0])
            q_y.append(j+ind[1])
            B[i+ind[0],j+ind[1]]=0
            ones+=1
    return ones

basins = []
B = (A!=9).astype(int)
while B.sum()>0:
    start = np.argwhere(B==1)[0]
    B[start[0],start[1]]=0
    count=1
    qX = [start[0]]
    qY = [start[1]]
    while len(qX)>0:
        count +=get_surround(B,qX.pop(),qY.pop(),qX,qY)
    basins.append(count)
basins.sort()
ans_2 = basins[-1]*basins[-2]*basins[-3]

print('Part 1: {}'.format(ans_1))
print('Part 2: {}'.format(ans_2))