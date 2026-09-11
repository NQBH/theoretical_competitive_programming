import random
from collections import defaultdict, deque

class RollbackDSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.sz = [1] * (n + 1)
        self.history = []

    def find(self, u):
        while u != self.parent[u]:
            u = self.parent[u]
        return u

    def unite(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u == v:
            self.history.append((-1, 0, 0))
            return False
        if self.sz[u] < self.sz[v]:
            u, v = v, u
        self.history.append((u, v, self.sz[u]))
        self.parent[v] = u
        self.sz[u] += self.sz[v]
        return True

    def rollback(self):
        if not self.history: return
        u, v, prev_sz = self.history.pop()
        if u == -1: return
        self.parent[v] = v
        self.sz[u] = prev_sz

class GraphOracle:
    def __init__(self):
        self.adj = defaultdict(list)
        self.history = []

    def add_edge(self, u, v):
        self.history.append((u, v))
        self.adj[u].append(v)
        self.adj[v].append(u)

    def rollback(self):
        if not self.history: return
        u, v = self.history.pop()
        self.adj[u].remove(v)
        self.adj[v].remove(u)

    def is_connected(self, u, v):
        visited = set([u])
        q = deque([u])
        while q:
            curr = q.popleft()
            if curr == v: return True
            for nxt in self.adj[curr]:
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)
        return False

def run_fuzzer(trials=100):
    print("[Module 05: Rollback DSU] Validating dynamic undo connectivity with multigraph / cycle edges...")
    for t in range(trials):
        n = random.randint(5, 15)
        dsu = RollbackDSU(n)
        oracle = GraphOracle()
        
        for _ in range(50):
            op = random.choices(['add', 'rollback', 'check'], weights=[0.6, 0.2, 0.2])[0]
            if op == 'add':
                u = random.randint(1, n)
                v = random.randint(1, n)
                dsu.unite(u, v)
                oracle.add_edge(u, v)
            elif op == 'rollback':
                dsu.rollback()
                oracle.rollback()
            elif op == 'check':
                u = random.randint(1, n)
                v = random.randint(1, n)
                assert (dsu.find(u) == dsu.find(v)) == oracle.is_connected(u, v)
    print("  -> Passed Fuzzer Semantic Match assertions (cycles & rollbacks).")

if __name__ == "__main__":
    run_fuzzer(500)
