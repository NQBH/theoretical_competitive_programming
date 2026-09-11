import random

def brute_force_subarray_sum(a, S):
    if S <= 0: return (-1, -1)
    n = len(a)
    for l in range(n):
        s = 0
        for r in range(l, n):
            s += a[r]
            if s == S:
                return (l + 1, r + 1)
    return (-1, -1)

def two_pointers_solve(a, S):
    if S <= 0: return (-1, -1)
    n = len(a)
    l, cur = 0, 0
    for r in range(n):
        cur += a[r]
        while cur > S and l <= r:
            cur -= a[l]
            l += 1
        if cur == S:
            return (l + 1, r + 1)
    return (-1, -1)

def run_tests():
    print("[Module 01: Two Pointers] Running stress testing...")
    for trial in range(500):
        n = random.randint(1, 150)
        a = [random.randint(1, 40) for _ in range(n)]
        S = random.randint(1, sum(a) + 10)
        ans_brute = brute_force_subarray_sum(a, S)
        ans_opt = two_pointers_solve(a, S)
        if ans_opt != (-1, -1):
            l, r = ans_opt
            assert sum(a[l-1:r]) == S
        else:
            assert ans_brute == (-1, -1)
    print("  -> Passed 500 randomized trials.")

if __name__ == "__main__":
    run_tests()
