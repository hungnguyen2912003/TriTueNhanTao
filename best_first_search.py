from utils.readfile import *
from utils.check import checkin

def bfs(adj, start, stop):
    OPEN = []
    CLOSE = []
    Tn = []
    Parent = [-1] * n
    OPEN.append(start)
    while len(OPEN) > 0:
        curr = OPEN.pop(0)
        print(f"curr: {curr}")
        print(f"Parent: {Parent}")
        if curr == stop:
            print(f"Tìm thấy đường đi")
            path = []
            idx = stop
            while idx != -1:
                path.insert(0, idx)
                idx = Parent[idx]
            print(f"Path: {path}")
            return
        CLOSE.append(curr)
        print(f"CLOSE: {CLOSE}")
        for neighbor in range(n):
            if adj[curr][neighbor] == 1 and checkin(OPEN, neighbor) == False and checkin(CLOSE, neighbor) == False:
                Tn.append(neighbor)
                Parent[neighbor] = curr
        print(f"Tập đỉnh kề: {Tn}")
        OPEN = Tn + OPEN
        OPEN_sorted = sorted(OPEN, key=lambda x: h[x][1])
        OPEN = OPEN_sorted
        print(f"OPEN: {OPEN_sorted}")
        Tn = []
    print(f"Không tìm thấy đường đi")


if __name__ == '__main__':
    n, adj = readfile_adj('inputs/bestfirstsearch.adj')
    print(f"Number of nodes: {n}")
    for i in range(n):
        print(f"Node {i}: {adj[i]}")
    h = read_h('inputs/bestfirstsearch.h')
    bfs(adj, 0, 7)