import numpy as np

fname = 'Day13/inp.txt'

footer = 0
B = []
for line in reversed(list(open(fname))):
    fold = line.rstrip()
    if fold=='':
        pass
    elif fold[0]=='f':
        footer+=1
        B.append(fold.split('='))
B.reverse()

input_array = np.genfromtxt(fname, dtype=str,skip_footer=footer)
A = []

for row in input_array:
    A.append(row.split(','))
A = np.array(A,dtype=int)

paper = np.zeros(np.amax(A,axis=0)+1,dtype=int)
for row in A:
    paper[row[0], row[1]] = 1

for i in range(len(B)):
    fold = B[i]
    if fold[0][-1]=='x':
        x = int(fold[1])
        new_paper = np.zeros((x,paper.shape[1])) + paper[0:x,:] + np.flipud(paper[x+1:,:])
    elif fold[0][-1]=='y':
        y = int(fold[1])
        new_paper = np.zeros((paper.shape[0],y)) + paper[:,0:y] + np.fliplr(paper[:,y+1:])
    del paper
    paper = new_paper
    del new_paper
    if i==0:
        ans_1 = (paper>0).astype(int).sum()

print('Part 1: {}'.format(ans_1))
print('Part 2:')
syms = [' ','#']
np.set_printoptions(linewidth=100,formatter={'all': lambda x: syms[x]})
print((paper>0).transpose().astype(int))