import sys
import random
sys.setrecursionlimit(200000)

def recursive_tree_dp(n, adj):
    dp = [[0, 0] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    
    def dfs(u):
        visited[u] = True
        dp[u][1] = 1
        for v in adj[u]:
            if not visited[v]:
                dfs(v)
                dp[u][0] += max(dp[v][0], dp[v][1])
                dp[u][1] += dp[v][0]
                
    dfs(1)
    return max(dp[1][0], dp[1][1])

def flat_tree_dp(n, adj):
    parent = [0] * (n + 1)
    topo = []
    visited = [False] * (n + 1)
    
    q = [1]
    visited[1] = True
    head = 0
    while head < len(q):
        u = q[head]
        head += 1
        topo.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                q.append(v)
                
    dp = [0] * (2 * (n + 1))
    for i in range(len(topo) - 1, -1, -1):
        u = topo[i]
        dp[2 * u + 1] = 1
        for v in adj[u]:
            if v != parent[u]:
                dp[2 * u] += max(dp[2 * v], dp[2 * v + 1])
                dp[2 * u + 1] += dp[2 * v]
                
    return max(dp[2], dp[3])

def generate_random_tree(n):
    adj = [[] for _ in range(n + 1)]
    is_pathological = (random.random() < 0.2)
    is_disconnected = (random.random() < 0.1)
    for i in range(2, n + 1):
        if is_disconnected and random.random() < 0.05:
            continue
        if is_pathological:
            p = i - 1
        else:
            p = random.randint(1, i - 1)
        adj[p].append(i)
        adj[i].append(p)
    return adj

def test_tree_dp(trials=100):
    for trial in range(trials):
        if trial < 2:
            n = 50000
        else:
            n = random.randint(1, 100)
        adj = generate_random_tree(n)
        res1 = recursive_tree_dp(n, adj)
        res2 = flat_tree_dp(n, adj)
        assert res1 == res2, f"Mismatch on trial {trial}"
    print(f"Tree DP fuzzer passed {trials} trials.")

if __name__ == "__main__":
    test_tree_dp()
