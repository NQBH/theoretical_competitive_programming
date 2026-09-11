def solve_naive_submasks(a, n):
    f = [0] * (1 << n)
    for mask in range(1 << n):
        sub = mask
        while True:
            f[mask] += a[sub]
            if sub == 0: break
            sub = (sub - 1) & mask
    return f

def solve_sos_dp(a, n):
    dp = list(a)
    for i in range(n):
        for mask in range(1 << n):
            if mask & (1 << i):
                dp[mask] += dp[mask ^ (1 << i)]
    return dp

def run_tests():
    print("[Module 08: Bitmask SOS DP] Comparing O(3^N) naive vs O(N 2^N) SOS DP...")
    n = 10
    a = [i + 1 for i in range(1 << n)]
    ans_naive = solve_naive_submasks(a, n)
    ans_sos = solve_sos_dp(a, n)
    assert ans_naive == ans_sos
    print("  -> Passed exact equivalence over all 1024 hypercube submasks.")

if __name__ == "__main__":
    run_tests()
