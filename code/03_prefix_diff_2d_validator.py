import random
import numpy as np

def solve_grid_naive(n, m, updates, queries):
    grid = [[0] * (m + 1) for _ in range(n + 1)]
    for x1, y1, x2, y2, v in updates:
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                grid[i][j] += v
    res = []
    for x1, y1, x2, y2 in queries:
        s = sum(grid[i][j] for i in range(x1, x2 + 1) for j in range(y1, y2 + 1))
        res.append(s)
    return res

def solve_grid_numpy(n, m, updates, queries):
    grid = np.zeros((n + 1, m + 1), dtype=np.int64)
    for x1, y1, x2, y2, v in updates:
        grid[x1:x2 + 1, y1:y2 + 1] += v
    res = []
    for x1, y1, x2, y2 in queries:
        res.append(int(grid[x1:x2 + 1, y1:y2 + 1].sum()))
    return res

def solve_grid_prefix(n, m, updates, queries):
    D = [[0] * (m + 2) for _ in range(n + 2)]
    for x1, y1, x2, y2, v in updates:
        D[x1][y1] += v
        D[x2+1][y1] -= v
        D[x1][y2+1] -= v
        D[x2+1][y2+1] += v
    Pref = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] += D[i-1][j] + D[i][j-1] - D[i-1][j-1]
            Pref[i][j] = D[i][j] + Pref[i-1][j] + Pref[i][j-1] - Pref[i-1][j-1]
    res = []
    for x1, y1, x2, y2 in queries:
        s = Pref[x2][y2] - Pref[x1-1][y2] - Pref[x2][y1-1] + Pref[x1-1][y1-1]
        res.append(s)
    return res

def run_tests():
    print("[Module 03: 2D Prefix & Difference] Running grid integration validator...")
    n, m = 15, 15
    updates = []
    for _ in range(20):
        x_a, x_b = random.randint(1, n), random.randint(1, n)
        y_a, y_b = random.randint(1, m), random.randint(1, m)
        updates.append((min(x_a, x_b), min(y_a, y_b), max(x_a, x_b), max(y_a, y_b), random.randint(1, 50)))
    queries = []
    for _ in range(30):
        x_a, x_b = random.randint(1, n), random.randint(1, n)
        y_a, y_b = random.randint(1, m), random.randint(1, m)
        queries.append((min(x_a, x_b), min(y_a, y_b), max(x_a, x_b), max(y_a, y_b)))
    naive_res = solve_grid_naive(n, m, updates, queries)
    prefix_res = solve_grid_prefix(n, m, updates, queries)
    numpy_res = solve_grid_numpy(n, m, updates, queries)
    assert naive_res == prefix_res == numpy_res, "Mismatch between Naive, Prefix, and NumPy oracles"
    print("  -> Passed 2D overlapping range updates and queries (including NumPy oracle).")

if __name__ == "__main__":
    run_tests()
