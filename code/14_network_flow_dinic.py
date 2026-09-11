def edmonds_karp(C, s, t):
    if s == t: return 0
    n = len(C)
    F = [[0] * n for i in range(n)]
    
    def bfs():
        from collections import deque
        queue = deque([s])
        parent = {s: -1}
        while queue:
            u = queue.popleft()
            for v in range(n):
                if (C[u][v] - F[u][v] > 0) and v not in parent:
                    parent[v] = u
                    if v == t:
                        return parent
                    queue.append(v)
        return None

    parent = bfs()
    while parent is not None:
        path = []
        curr = t
        while curr != s:
            p = parent[curr]
            path.append((p, curr))
            curr = p
        path.reverse()
        
        flow = min(C[u][v] - F[u][v] for u, v in path)
        for u, v in path:
            F[u][v] += flow
            F[v][u] -= flow
        parent = bfs()
    return sum(F[s][i] for i in range(n))

import random
import networkx as nx

def generate_flow_network(n, m, max_cap):
    G = nx.DiGraph()
    G.add_nodes_from(range(n))
    edges_added = 0
    while edges_added < m:
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        while u == v:
            v = random.randint(0, n - 1)
        c = random.randint(1, max_cap)
        if not G.has_edge(u, v):
            G.add_edge(u, v, capacity=c)
            edges_added += 1
    return G

def run_tests():
    print("[Module 14: Network Flow & Matching] Fuzzing Network Flow...")
    for _ in range(100):
        n = random.randint(4, 20)
        m = random.randint(n, n * (n - 1) // 2)
        G = generate_flow_network(n, m, 20)
        C = [[0] * n for _ in range(n)]
        for u, v, data in G.edges(data=True):
            C[u][v] = data['capacity']
        
        s, t = 0, n - 1
        nx_flow_val = nx.maximum_flow_value(G, s, t)
        my_flow_val = edmonds_karp(C, s, t)
        assert nx_flow_val == my_flow_val
        
        # S=T Edge Case
        assert edmonds_karp(C, 0, 0) == 0
        
    print("  -> Passed Max Flow Fuzzing against NetworkX oracle.")

if __name__ == "__main__":
    run_tests()
