import numpy as np
from statistics import median

from numpy.core.numeric import argwhere
fname = 'Day8/inp.txt'

input_array = np.genfromtxt(fname, dtype=str, delimiter='|')

in_array = []
out_array = []
for i in range(input_array.shape[0]):
    in_array.append(input_array[i,0].split(' '))
    out_array.append(input_array[i,1].split(' '))
in_array = np.array(in_array)
out_array = np.array(out_array)

count = 0
for i in range(out_array.shape[0]):
    for j in range(out_array[i].shape[0]):
        if len(out_array[i,j])==2 or len(out_array[i,j])==3 or len(out_array[i,j])==4 or len(out_array[i,j])==7:
            count+=1

ans_1=count

#  000
# 1   2
# 1   2
#  333
# 4   5
# 4   5
#  666
#print(in_array[0], out_array[0])

seg2num = np.array([
    '012456',
    '25',
    '02346',
    '02356',
    '1235',
    '01356',
    '013456',
    '025',
    '0123456',
    '012356'
],dtype=str)

ans_2 = 0


for i in range(out_array.shape[0]):
    
    total_set = {'a','b','c','d','e','f','g'}
    sets = []
    for j in range(7):
        sets.append(total_set.copy())
    new_set = set()
    len_5 = []
    len_6 = []
    for j in range(in_array[i].shape[0]):
        if len(in_array[i,j])==2:
            for char in in_array[i,j]: new_set.add(char)
            for k in [2,5]: sets[k].intersection_update(new_set)
        if len(in_array[i,j])==3:
            for char in in_array[i,j]: new_set.add(char)
            for k in [0,2,5]: sets[k].intersection_update(new_set)
        if len(in_array[i,j])==4:
            for char in in_array[i,j]: new_set.add(char)
            for k in [1,2,3,5]: sets[k].intersection_update(new_set)
        if len(in_array[i,j])==5:
            for char in in_array[i,j]: new_set.add(char)
            len_5.append(new_set.copy())
        if len(in_array[i,j])==6:
            for char in in_array[i,j]: new_set.add(char)
            len_6.append(new_set.copy())
        new_set.clear()

    sets[0].difference_update(sets[2])
    for j in range(1,7): sets[j].difference_update(sets[0])
    for j in [1,3,4,6]: sets[j].difference_update(sets[2])
    
    for line in len_5:
        if len(sets[2].intersection(line))==2:
            mids = line.difference(sets[2]).copy()
            for j in [3,6]: sets[j].intersection_update(line.difference(sets[2]))
            for j in [1,4,6]: sets[j].difference_update(sets[3])
            for j in [1,4]: sets[j].difference_update(sets[6])
            sets[4].difference_update(sets[1])
    

    for line in len_5:
        if len(line.intersection(sets[4].copy().union(sets[3].copy())))==2:
            sets[2].intersection_update(line)
            sets[5].difference_update(sets[2])

    seg_disp = np.array(list(map(list,sets))).flatten()

    output = ''
    for digit in out_array[i,1:]:
        digit_seg = []
        for j in range(len(digit)):
            digit_seg.append(np.argwhere(digit[j]==seg_disp)[0][0])
        digit_seg.sort()
        seg_str = ''
        for chars in digit_seg: seg_str+=str(chars)
        output += str(np.argwhere(seg_str==seg2num)[0,0])
    ans_2+=int(output)


print('Part 1: {}'.format(ans_1))
print('Part 2: {}'.format(ans_2))