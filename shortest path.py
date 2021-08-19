import queue
queries = int(input())
for _ in range(queries):
    n, m = map(int, input().split())
    visited = [False for i in range(2000)]
    dist = [-1 for i in range(2000)]
    graph = [[] for i in range(2000)]
    q = queue.Queue()
    def bfs(s):
        visited[s] = True
        q.put(s)
        dist[s] = 0
        while not q.empty():
            u = q.get()
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    dist[v] = dist[u] + 6
                    q.put(v)
        return [dist[i] for i in range(1, n+1) if i != s]
    if __name__ == "__main__":
        for _ in range(m):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)
        s = int(input())
        result = bfs(s)
        print(" ".join(map(str, result)))