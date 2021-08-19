import queue
def bfs(s):
    leaves = 0
    q = queue.Queue()
    visited[s] = True
    q.put(s)
    if a[s] == 1:
        cats[s] = 1
    else:
        cats[s] = 0
    while not q.empty():
        x = q.get()
        for y in graph[x]:
            if not visited[y]:
                visited[y] = True
                if a[y] == 1:
                    cats[y] = cats[x] + 1
                if cats[y] <= m:
                    if len(graph[y]) == 1:
                        leaves += 1
                    else:
                        q.put(y)
    return leaves

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    visited = [False for _ in range(n)]
    cats = [0 for _ in range(n)]
    graph = [[] for _ in range(n)]
    for i in range(1, n):
        x, y = map(int, input().split())
        x, y = x-1, y-1
        graph[x].append(y)
        graph[y].append(x)
    print(bfs(0))