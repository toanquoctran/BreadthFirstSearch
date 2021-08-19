import queue
t = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    places = 1
    visited[x][y] = True
    q = queue.Queue()
    q.put((x, y))
    while not q.empty():
        curx, cury = q.get()
        for i in range(4):
            newx = curx + dx[i]
            newy = cury + dy[i]
            if 0 <= newx <= h-1 and 0 <= newy <= w-1 and maze[newx][newy] == "." \
                    and not visited[newx][newy]:
                visited[newx][newy] = True
                places += 1
                q.put((newx, newy))
    return places
for case in range(t):
    w, h = map(int, input().split())
    visited = [[False for _ in range(w)] for i in range(h)]
    maze = [None] * h
    x = 0
    y = 0
    for i in range(h):
        maze[i] = input()
        for j in range(w):
            if maze[i][j] == "@":
                x = i
                y = j
    res = bfs(x, y)
    print("Case {}: {}".format(case+1, res))