import queue
def bfs():
    q = queue.Queue()
    q.put((sx, sy))
    while not q.empty():
        curx, cury = q.get()
        for i in range(4):
            newx = curx + dx[i]
            newy = cury + dy[i]
            if 0 < newx+1 <= n and 0 < newy+1 <= m:
                if maze[newx][newy] == "X" and newx == fx and newy == fy:
                    return True
                elif maze[newx][newy] == ".":
                    maze[newx][newy] = "X"
                    q.put((newx, newy))
    return False

if __name__ == "__main__":
    n, m = map(int, input().split())
    maze = [None] * n
    for i in range(n):
        maze[i] = list(input())
    sx, sy = map(int, input().split())
    fx, fy = map(int, input().split())
    sx -= 1
    sy -= 1
    fx -= 1
    fy -= 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    if bfs():
        print("YES")
    else:
        print("NO")