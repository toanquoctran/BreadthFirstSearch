import queue
def bfs(x, y):
    visited[x][y] = True
    q = queue.Queue()
    q.put((x, y))
    slickSize = 1
    while not q.empty():
        curx, cury = q.get()
        for i in range(4):
            newx = curx + dx[i]
            newy = cury + dy[i]
            if 0 < newx+1 <= n and 0 < newy+1 <= m and not visited[newx][newy]:
                if maze[newx][newy] == "1":
                    visited[newx][newy] = True
                    slickSize += 1
                    q.put((newx, newy))
    area[slickSize] += 1

while True:
    n, m = map(int, input().split())
    area = [0] * 62501
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    num = 0
    if n == 0:
        break
    visited = [[False for _ in range(m)] for i in range(n)]
    maze = [None] * n
    for i in range(n):
        maze[i] = list(input().split())
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maze[i][j] == "1":
                maze[i][j] = 0
                bfs(i, j)
                num += 1
    print(num)
    for i in range(62501):
        if area[i] != 0:
            print("{} {}".format(i, area[i]))