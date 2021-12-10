import numpy as np

fname = 'Day10/inp.txt'

input_array = np.genfromtxt(fname, dtype=str)


char_dict = {'(': 1,
             '[': 2,
             '{': 3,
             '<': 4,
             ')': 5,
             ']': 6,
             '}': 7,
             '>': 8}

score_dict = {')': 3,
              ']': 57,
              '}': 1197,
              '>': 25137}

ans_1 = 0

rowVals = []
for ct,row in enumerate(input_array):
    i=0
    looping = True
    corrupted = False
    q = []
    while looping:
        num = char_dict[row[i]]
        if num<5:
            q.append(num)
        if num>4:
            if q[-1]==num-4:
                q = q[:-1]
            else:
                looping=False
                ans_1 += score_dict[row[i]]
                corrupted = True
        i+=1
        if i>=len(row):
            looping=False
    if len(q)>0 and not corrupted:
        rowVal = 0
        for item in q[::-1]:
            rowVal = rowVal*5 + item
        rowVals.append(rowVal)
   

rowVals.sort()
ans_2 = rowVals[len(rowVals)//2]


print('Part 1: {}'.format(ans_1))
print('Part 2: {}'.format(ans_2))