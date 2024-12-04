from utils.readfile import *
from utils.check import checkin


def NhanhCan(adj, start, stop):
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
    flag = False
    fmin = float('inf')

    while len(OPEN) > 0:
        curr = OPEN.pop(0)
        print(f"curr: {curr}")
        CLOSE.append(curr)
        print(f"CLOSE: {CLOSE}")

        if curr == stop:
            flag = True
            if f[curr] < fmin:
                fmin = f[curr]


        for neighbor in range(len(adj)):
            if adj[curr][neighbor] != 0:
                # n không thuộc OPEN và CLOSE
                if f[curr] < fmin and checkin(OPEN, neighbor) == False and checkin(CLOSE, neighbor) == False:
                    Tn.append(neighbor)
                    g[neighbor] = g[curr] + adj[curr][neighbor]
                    f[neighbor] = g[neighbor] + h[neighbor][1]
                    Parent[neighbor] = curr
                # n thuộc OPEN (không quan tâm đến CLOSE)
                if f[curr] < fmin and checkin(OPEN, neighbor) == True:
                    g_new = g[curr] + adj[curr][neighbor]
                    f_new = g_new + h[neighbor][1]
                    if f_new < f[neighbor]:
                        g[neighbor] = g_new
                        f[neighbor] = f_new
                        print(f"Cập nhật giá trị f({neighbor}), g({neighbor})")
                        print(f"g_new({neighbor}): {g_new}, f_new({neighbor}): {f_new}")
                        Parent[neighbor] = curr #Cập nhật Parent và không đưa vào Tn
                # n không thuộc OPEN nhưng thuộc CLOSE
                if f[curr] < fmin and checkin(OPEN, neighbor) == False and checkin(CLOSE, neighbor) == True:
                    Tn.append(neighbor)
                    g[neighbor] = g[curr] + adj[curr][neighbor]
                    f[neighbor] = g[neighbor] + h[neighbor][1]
                    if neighbor == stop:
                        Parent[neighbor] = curr


        print(f"Tn: {Tn}")

        # Chèn Tn vào đầu OPEN
        OPEN = Tn + OPEN
        print(f"OPEN: {OPEN}")

        # Không sắp xếp OPEN tăng dần theo f
        Tn_sorted = sorted(Tn, key=lambda x: f[x], reverse=False)
        OPEN = Tn_sorted + OPEN
        print(f"g: {g}")
        print(f"f: {f}")
        print(f"Parent: {Parent}")

        # Reset Tn
        Tn = []

    #Kiểm tra giá trị flag
    if flag == False:
        print(f"Không tìm thấy đường đi {start} -> {stop}")
    else:
        print(f"Tìm thấy đường đi {start} -> {stop}")
        path = []
        idx = stop
        while idx != start:
            path.insert(0, idx)
            idx = Parent[idx]
        path.insert(0, start)
        print(f"path: {path}")


if __name__ == '__main__':
    n, adj = readfile_adj('inputs/nhanhCan.adj')
    h = read_h('inputs/nhanhCan.h')
    print(f"Number of nodes: {n}")
    print(f"Heuristic: {h}")
    print(f"Adjacency list: ")
    for i in range(n):
        print(f"{adj[i]}")

    NhanhCan(adj, 0, 7)