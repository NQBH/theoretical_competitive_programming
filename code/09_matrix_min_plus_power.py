def min_plus_mult(A, B, n):
    C = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k] == float('inf'): continue
            for j in range(n):
                C[i][j] = min(C[i][j], A[i][k] + B[k][j])
    return C

def min_plus_power(A, n, p):
    res = [[float('inf')] * n for _ in range(n)]
    for i in range(n): res[i][i] = 0
    base = [row[:] for row in A]
    while p > 0:
        if p & 1: res = min_plus_mult(res, base, n)
        base = min_plus_mult(base, base, n)
        p >>= 1
    return res

def run_tests():
    print("[Module 09: Min-Plus Matrix Exponentiation] Validating shortest path with exact steps...")
    n = 3
    inf = float('inf')
    A = [
        [inf, 2, 5],
        [inf, inf, 1],
        [inf, inf, inf]
    ]
    res2 = min_plus_power(A, n, 2)
    assert res2[0][2] == 3 # 0 -> 1 -> 2 with cost 2+1=3
    print("  -> Passed min-plus associative exponentiation.")

if __name__ == "__main__":
    run_tests()
