import queue
def bfs(x, y):
    visited[x][y] = True
    q = queue.Queue()
    q.put((x, y))
    canEscape = False
    countSheep = 0
    countWolves = 0
    if maze[x][y] == "k":
        countSheep += 1
    if maze[x][y] == "v":
        countWolves += 1
    while not q.empty():
        curx, cury = q.get()
        if curx == 0 or curx == n - 1 or cury == 0 or cury == m - 1:
            canEscape = True
        for i in range(4):
            newx = curx + dx[i]
            newy = cury + dy[i]
            if 0 <= newx < n and 0 <= newy < m:
                if maze[newx][newy] != "#" and not visited[newx][newy]:
                    visited[newx][newy] = True
                    if maze[newx][newy] == "k":
                        countSheep += 1
                    elif maze[newx][newy] == "v":
                        countWolves += 1
                    q.put((newx, newy))
    if canEscape:
        return countSheep, countWolves
    else:
        if countSheep > countWolves:
            return countSheep, 0
        else:
            return 0, countWolves

n, m = map(int, input().split())
maze = [None] * n
for i in range(n):
    maze[i] = list(input())
visited = [[False for _ in range(m)] for i in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
sheep = 0
wolves = 0
resSheep = 0
resWolves = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and maze[i][j] == "." or maze[i][j] == "k" \
                and maze[i][j] == "v":
            maze[i][j] = "#"
            resSheep, resWolves = bfs(i, j)
            sheep += resSheep
            wolves += resWolves
print(sheep, wolves)