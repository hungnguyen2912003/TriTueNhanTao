from utils.readfile import *
from utils.check import checkin


def ASTAR(adj, start, stop):
    OPEN = []
    CLOSE = []
    Tn = []
    Parent = [-1] * len(adj)
    g = [float('inf')] * len(adj)
    f = [float('inf')] * len(adj)

    # Step 0:
    OPEN.append(start)
    g[start] = 0
    f[start] = h[start][1]

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
            if adj[curr][neighbor] != 0:
                if checkin(OPEN, neighbor) == False and checkin(CLOSE, neighbor) == False:
                    Tn.append(neighbor)
                    g[neighbor] = g[curr] + adj[curr][neighbor]
                    f[neighbor] = g[neighbor] + h[neighbor][1]
                    Parent[neighbor] = curr
                else:  #neighbor thuộc về OPEN hoặc CLOSE
                    g_new = g[curr] + adj[curr][neighbor]
                    f_new = g_new + h[neighbor][1]
                    print(f"g_new({neighbor}): {g_new}, f_new({neighbor}): {f_new}")

                    if f_new < f[neighbor]:
                        g[neighbor] = g_new
                        f[neighbor] = f_new
                        print(f"Cập nhật giá trị f({neighbor}), g({neighbor})")
                        Parent[neighbor] = curr #Cập nhật Parent và không đưa vào Tn


        print(f"Tn: {Tn}")

        # Chèn Tn vào đầu OPEN
        OPEN = Tn + OPEN
        print(f"OPEN: {OPEN}")

        # Sắp xếp OPEN tăng dần theo f
        OPEN_sorted = sorted(OPEN, key=lambda x: f[x], reverse=False)
        OPEN = OPEN_sorted
        print(f"OPEN_sorted: {OPEN}")
        print(f"g: {g}")
        print(f"f: {f}")
        print(f"Parent: {Parent}")

        # Reset Tn
        Tn = []

    # OPEN = 0
    print(f"Không tìm thấy đường đi {start} -> {stop}")


if __name__ == '__main__':
    n, adj = readfile_adj('inputs/astar.adj')
    h = read_h('inputs/astar.h')
    print(f"Number of nodes: {n}")
    print(f"Heuristic: {h}")
    print(f"Adjacency list: ")
    for i in range(n):
        print(f"{adj[i]}")

    ASTAR(adj, 0, 6)