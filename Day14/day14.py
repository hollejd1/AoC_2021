import numpy as np

fname = 'Day14/inp.txt'

with open(fname, 'r') as file:
    header = file.readline()[:-1]

input_array = np.genfromtxt(fname, dtype=str, delimiter=' -> ', skip_header=2)
translate = dict(input_array)

A = header
for n in range(10):
    B = A[0]
    for i in range(len(A)-1):
        key = A[i:i+2]
        newChar = translate[key]
        B += newChar + key[1]
    A = B

elements = ''.join(set(A))
counts = []
for element in elements:
    counts.append(A.count(element))

ans_1 = max(counts) - min(counts)

C = np.zeros((input_array.shape[0],1),dtype=int)
for i in range(len(header)-1):
    key = header[i:i+2]
    inds = np.argwhere(input_array[:,0]==key)[0][0]
    C[inds] +=1

for n in range(40):
    D = np.zeros_like(C,dtype=int)
    for i in range(C.shape[0]):
        key = input_array[i,0]
        newChar = input_array[i,1]
        ind1 = np.argwhere(input_array[:,0]==(key[0]+newChar))[0][0]
        ind2 = np.argwhere(input_array[:,0]==(newChar+key[1]))[0][0]
        D[ind1] += C[i]
        D[ind2] += C[i]
    C = D

element_list = np.array(list(elements))
counts_2 = np.zeros_like(element_list, dtype=np.longlong)
for i in range(input_array.shape[0]):
    counts_2[np.argwhere(element_list==input_array[i,0][0])[0][0]] += C[i]
counts_2[np.argwhere(element_list==header[-1])[0][0]] += 1

ans_2 = max(counts_2) - min(counts_2)

print('Part 1: {}'.format(ans_1))
print('Part 2: {}'.format(ans_2))