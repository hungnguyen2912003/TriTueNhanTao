from utils.readfile import *
from utils.check import checkin

def AT(adj, start, stop):
    OPEN = []
    CLOSE = []
    Tn = []
    Parent = [-1] * len(adj)
    g = [float('inf')] * len(adj)

    #Step 0:
    OPEN.append(start)
    g[start] = 0

    while len(OPEN) > 0:
        curr = OPEN.pop(0)
        print(f"curr: {curr}")
        CLOSE.append(curr)
        print(f"CLOSE: {CLOSE}")

        if curr == stop:
            print(f"Tìm thấy đường đi {start} -> {stop}")
            path = []
            idx = stop
            while idx != -1:
                path.insert(0, idx)
                idx = Parent[idx]
            print(f"path: {path}")
            return
        for neighbor in range(len(adj)):
            if adj[curr][neighbor] == 1 and checkin(OPEN, neighbor) == False and checkin(CLOSE, neighbor) == False:
                Tn.append(neighbor)
                g[neighbor] = g[curr] + h[neighbor][1]
                Parent[neighbor] = curr
                
        print(f"Tn: {Tn}")

        #Chèn Tn vào đầu OPEN
        OPEN = Tn + OPEN
        print(f"OPEN: {OPEN}")

        #Sắp xếp OPEN tăng dần theo g
        OPEN_sorted = sorted(OPEN, key = lambda x: g[x], reverse = False)
        OPEN = OPEN_sorted
        print(f"OPEN_sorted: {OPEN}")
        print(f"g: {g}")

        #Reset Tn
        Tn = []

    # OPEN = 0
    print(f"Không tìm thấy đường đi {start} -> {stop}")

if __name__ == '__main__':
    n, adj = readfile_adj('inputs/at.adj')
    print(f"Number of nodes: {n}")
    for i in range(n):
        print(f"Node {i}: {adj[i]}")
    h = read_h('inputs/at.h')
    AT(adj, 0, 6)