import queue
T = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, z, t):
    visited[x][y] = True
    q = queue.Queue()
    q.put((x, y))
    while not q.empty():
        curx, cury = q.get()
        for i in range(4):
            newx = curx + dx[i]
            newy = cury + dy[i]
            if 0 <= newx <= m-1 and 0 <= newy <= n-1 and maze[newx][newy] == "." and not visited[newx][newy]:
                visited[newx][newy] = True
                if newx == z and newy == t:
                    return True
                q.put((newx, newy))
    return False

for _ in range(T):
    m, n = map(int, input().split())
    visited = [[False for _ in range(n)] for i in range(m)]
    entrance = set()
    maze = [None] * m
    count = 0

    for i in range(m):
        maze[i] = input()
    for j in range(n):
        if maze[0][j] == ".":
            entrance.add((0, j))
        if maze[m - 1][j] == ".":
            entrance.add((m - 1, j))
    for i in range(m):
        if maze[i][0] == ".":
            entrance.add((i, 0))
        if maze[i][n - 1] == ".":
            entrance.add((i, n - 1))
    if len(entrance) != 2:
        print("invalid")
    else:
        entrance = list(entrance)
        x, y = entrance[0]
        z, t = entrance[1]
        result = bfs(x, y, z, t)
        if result:
            print("valid")
        else:
            print("invalid")