import queue
s, b = map(int, input().split())
n = int(input())
v = list(map(int, input().split()))
visited = [False for i in range(100001)]
dist = [-1 for _ in range(100001)]
def bfs(s, b):
    q = queue.Queue()
    visited[s] = True
    q.put(s)
    dist[s] = 0
    while not q.empty():
        cur = q.get()
        for i in range(n):
            temp = cur * v[i]
            temp %= 100000
            if not visited[temp]:
                visited[temp] = True
                dist[temp] = dist[cur] + 1
                q.put(temp)
                if temp == b:
                    return dist[b]
    return dist[b]
if __name__ == "__main__":
    res = bfs(s, b)
    print(res)