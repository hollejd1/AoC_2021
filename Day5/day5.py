import numpy as np
from scipy import stats

fname = 'Day5/inp.txt'

input_array = np.genfromtxt(fname, dtype=str)

new_inp = []
for i in range(input_array.shape[0]):
    new_inp.append([input_array[i,0].split(','),input_array[i,2].split(',')])
new_inp = np.array(new_inp, dtype=int)

x = np.max(new_inp[:,:,0])+1
y = np.max(new_inp[:,:,1])+1

field = np.zeros((x,y),dtype=int)
field_2 = np.zeros((x,y),dtype=int)
for i, row in enumerate(new_inp):
    if row[0,0]==row[1,0]:
        x = row[0,0]
        y = range(row[:,1].min(),row[:,1].max()+1)
        field[x,y] +=1
        field_2[x,y] +=1
    if row[0,1]==row[1,1]:
        x = range(row[:,0].min(),row[:,0].max()+1)
        y = row[0,1]
        field[x,y] +=1
        field_2[x,y] +=1
    if (row[0,0]-row[1,0])**2 == (row[0,1]-row[1,1])**2:
        x_sign = (row[0,0]-row[1,0])//(abs(row[0,0]-row[1,0]))
        y_sign = (row[0,1]-row[1,1])//(abs(row[0,1]-row[1,1]))
        x = row[0,0]
        y = row[0,1]
        for i in range(abs(row[0,0]-row[1,0])+1):
            field_2[x,y] +=1
            x -= x_sign
            y -= y_sign

ans_1=(field>=2).astype(int).sum()
ans_2=(field_2>=2).astype(int).sum()

print('Part 1: {}'.format(ans_1))
print('Part 2: {}'.format(ans_2))