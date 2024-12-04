from utils.readfile import *
from utils.check import checkin

def bfs(adj, start, stop, type):
    OPEN = []
    CLOSE = []
    Tn = []
    Parent = [-1] * len(adj) #[-1 -1- 1 -1 ... -1]


    #Khởi tạo giá trị
    OPEN.append(start) #Đưa start vào cuối Open
    while len(OPEN) > 0: #OPEN khác rỗng

        curr = OPEN.pop(0) #Lấy ra ở đầu OPEN
        print(f"curr: {curr}")
        CLOSE.append(curr)
        print(f"CLOSE: {CLOSE}")
        if curr == stop:
            print(f"Tìm thấy đường đi")
            path = []
            idx = stop
            while idx != -1:
                path.insert(0, idx)
                idx = Parent[idx]
            print(f"path: {path}")
            return #Dừng vòng lặp

        #else: Chưa phải là đỉnh stop
        for neighbor in range(n):
            if adj[curr][neighbor] == 1 and checkin(OPEN,neighbor) == False and checkin(CLOSE,neighbor) == False:
                Tn.append(neighbor) #Đưa vào tập đỉnh kề
                Parent[neighbor] = curr
        print(f"Tập đỉnh kề: {Tn}")
        if type == "BFS":
            OPEN = OPEN + Tn #Chèn Tn vào cuối OPEN
        else:
            OPEN = Tn + OPEN #Chèn Tn vào đầu OPEN
        print(f"OPEN: {OPEN}")
        Tn = [] #reset Tn
        print(f"Parent: {Parent}")

    print("Không tìm thấy đường đi")


if __name__ == '__main__':
    n, adj = readfile_adj('inputs/bfs.adj')
    print(f"Number of nodes: {n}")
    for i in range(n):
        print(f"Node {i}: {adj[i]}")

    bfs(adj, 0, 6, "DFS")