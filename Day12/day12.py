import numpy as np

fname = 'Day12/inp.txt'

input_array = np.genfromtxt(fname, dtype=str)
A = []
for row in input_array:
    A.append(row.split('-'))
A = np.array(A,dtype=str)

nodes = np.unique(A)
G = []
for node in nodes:
    starts = np.argwhere(A[:,0]==node)
    ends = np.argwhere(A[:,1]==node)
    edges = np.concatenate((A[starts[:,0],1],A[ends[:,0],0]))
    G.append(edges)
G = np.array(G, dtype=object)

def search_caves(G, nodes, visited, curNode, duped):
    paths = 0
    visited = visited + [curNode]
    edges = G[np.argwhere(curNode==nodes)[0]]
    for edge in edges[0]:
        if edge=='end':
            paths+=1
        elif edge in visited:
            if edge[0].lower()!=edge[0]:
                paths += search_caves(G,nodes,visited,edge,duped)
            elif not duped and edge!='start':
                paths += search_caves(G,nodes,visited,edge, True)
        else:
            paths += search_caves(G,nodes,visited,edge,duped)
    return paths

curNode = nodes[np.argwhere(nodes=='start')[0,0]]
visited = []
ans_1 = search_caves(G,nodes,visited,curNode, True)

curNode = nodes[np.argwhere(nodes=='start')[0,0]]
visited = []
ans_2 = search_caves(G,nodes,visited,curNode, False)

print('Part 1: {}'.format(ans_1))
print('Part 2: {}'.format(ans_2))