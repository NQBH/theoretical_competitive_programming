import random

INF = 10**18

def w(j, i, a):
    s = sum(a[j:i])
    return s * s

def verify_monge_matrix(a, n):
    for x in range(n):
        for y in range(x, n):
            for z in range(y, n):
                for t in range(z, n):
                    val1 = w(x, z, a) + w(y, t, a)
                    val2 = w(x, t, a) + w(y, z, a)
                    assert val1 <= val2, "Monge property violated!"

def naive_dp(a, n, K):
    dp = [[INF] * (n + 1) for _ in range(K + 1)]
    dp[0][0] = 0
    for k in range(1, K + 1):
        for i in range(1, n + 1):
            for j in range(i):
                if dp[k - 1][j] != INF:
                    dp[k][i] = min(dp[k][i], dp[k - 1][j] + w(j, i, a))
    return dp

def compute_dnc(k, l, r, opt_l, opt_r, dp_prev, dp_cur, a):
    if l > r: return
    mid = (l + r) // 2
    best_k = opt_l
    dp_cur[mid] = INF
    
    for j in range(opt_l, min(mid - 1, opt_r) + 1):
        if dp_prev[j] == INF: continue
        val = dp_prev[j] + w(j, mid, a)
        if val < dp_cur[mid]:
            dp_cur[mid] = val
            best_k = j
            
    compute_dnc(k, l, mid - 1, opt_l, best_k, dp_prev, dp_cur, a)
    compute_dnc(k, mid + 1, r, best_k, opt_r, dp_prev, dp_cur, a)

def optimized_dp(a, n, K):
    dp_prev = [INF] * (n + 1)
    dp_prev[0] = 0
    for k in range(1, K + 1):
        dp_cur = [INF] * (n + 1)
        compute_dnc(k, 1, n, 0, n, dp_prev, dp_cur, a)
        dp_prev = dp_cur
    return dp_prev

def test_dnc_dp():
    n = 20
    K = 5
    for _ in range(100):
        a = [random.randint(1, 10) for _ in range(n)]
        
        verify_monge_matrix(a, n)
        
        ans_naive = naive_dp(a, n, K)[K]
        ans_opt = optimized_dp(a, n, K)
        
        for i in range(1, n + 1):
            assert ans_naive[i] == ans_opt[i], f"Mismatch at {i}: {ans_naive[i]} vs {ans_opt[i]}"
    print("Divide and Conquer DP passed stress testing.")

if __name__ == "__main__":
    test_dnc_dp()
