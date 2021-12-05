import numpy as np
from scipy import stats

fname = 'Day4/inp_test.txt'

f = open(fname,'r')
header = np.array(f.readline().split(','),dtype='int')
f.close()

input_array = np.genfromtxt(fname, dtype=int, skip_header=1)

input_boards = np.zeros(((input_array.shape[0])//5,5,5))
i = 0
j = 0
for row in input_array:
    if j==5:
        i+=1
        j=0
    input_boards[i,j,:] = row
    j+=1
input_boards = np.array(input_boards, dtype=int)

called = np.zeros_like(input_boards)
part_1 = True
part_2 = True
for i in range(header.shape[0]):
    called += (input_boards == header[i]).astype(int)
    bingo = np.unique(np.concatenate((np.argwhere(called.sum(axis=1).max(axis=1)==5),np.argwhere(called.sum(axis=2).max(axis=1)==5))))
    if bingo.shape[0]==1 and part_1:
        part_1=False
        ans_1 = header[i] * (input_boards[bingo[0]]*(~called[bingo[0]] + 2)).sum()
    if bingo.shape[0]==input_boards.shape[0]-1:
        finished = bingo
    if bingo.shape[0]==input_boards.shape[0] and part_2:
        part_2=False
        winner_2 = np.setdiff1d(bingo,finished)[0]
        ans_2 = header[i] * (input_boards[winner_2]*(~called[winner_2] + 2)).sum()



print('Part 1: {}'.format(ans_1))
print('Part 2: {}'.format(ans_2))
