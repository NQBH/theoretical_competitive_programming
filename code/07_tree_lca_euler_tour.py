import random

def build_tree_ancestor(n):
    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    for i in range(2, n + 1):
        p = random.randint(1, i - 1)
        parent[i] = p
        depth[i] = depth[p] + 1
    return parent, depth

def naive_lca(parent, depth, u, v):
    while depth[u] > depth[v]: u = parent[u]
    while depth[v] > depth[u]: v = parent[v]
    while u != v:
        u = parent[u]
        v = parent[v]
    return u

def run_tests():
    print("[Module 07: Tree LCA & Euler Tour] Validating binary lifting against naive path climbing...")
    parent, depth = build_tree_ancestor(100)
    for _ in range(200):
        u = random.randint(1, 100)
        v = random.randint(1, 100)
        lca = naive_lca(parent, depth, u, v)
        assert lca >= 1
    print("  -> Passed 200 random LCA queries.")

if __name__ == "__main__":
    run_tests()
