import random

INF = 10**18

def multiply_min_plus(A, B):
    n = len(A)
    C = [[INF] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k] == INF: continue
            for j in range(n):
                if B[k][j] != INF:
                    C[i][j] = min(C[i][j], A[i][k] + B[k][j])
    return C

def power_min_plus(A, p):
    n = len(A)
    res = [[INF] * n for _ in range(n)]
    for i in range(n): res[i][i] = 0
    base = A
    while p > 0:
        if p % 2 == 1:
            res = multiply_min_plus(res, base)
        base = multiply_min_plus(base, base)
        p //= 2
    return res

def naive_power_min_plus(A, p):
    n = len(A)
    res = [[INF] * n for _ in range(n)]
    for i in range(n): res[i][i] = 0
    for _ in range(p):
        res = multiply_min_plus(res, A)
    return res

def fuzzer():
    print("Running Min-Plus Matrix Exponentiation Fuzzer...")
    for test in range(50):
        n = random.randint(2, 10)
        p = random.randint(1, 20)
        A = [[INF] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    A[i][j] = 0
                elif random.random() < 0.5:
                    A[i][j] = random.randint(1, 100)
        
        res_fast = power_min_plus(A, p)
        res_naive = naive_power_min_plus(A, p)
        
        assert res_fast == res_naive, "Mismatch found!"
    print("All tests passed successfully.")

if __name__ == "__main__":
    fuzzer()
