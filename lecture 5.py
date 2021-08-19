import queue
V = None
E = None
q = queue.Queue()
visited = [False for _ in range(100)]
path = [-1 for _ in range(100)]
graph =[[] for _ in range(100)]
def BFS(s):
    for i in range(V):
        visited[i] = False
        path[i] = -1
    visited[s] = True
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.put(v)
                path[v] = u
def printPathRecursion(s, f):
    if s == f:
        print(f, end = " ")
    else:
        if path[f] == -1:
            print("No path")
        else:
            printPathRecursion(s, path[f])
            print(f, end = " ")
if __name__ == "__main__":
    V, E = map(int, input().split())
    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    s = 1
    f = 4
    BFS(s)
    printPathRecursion(s, f)