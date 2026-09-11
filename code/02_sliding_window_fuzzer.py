import random
from collections import deque

def brute_force_sliding_min(a, k):
    if k <= 0: return []
    return [min(a[i:i+k]) for i in range(len(a) - k + 1)]

def deque_sliding_min(a, k):
    if k <= 0: return []
    dq = deque()
    res = []
    for i, x in enumerate(a):
        if dq and dq[0] <= i - k:
            dq.popleft()
        while dq and a[dq[-1]] >= x:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            res.append(a[dq[0]])
    return res

def run_tests():
    print("[Module 02: Sliding Window] Running monotonic deque fuzzer...")
    for trial in range(300):
        n = random.randint(1, 200)
        k = random.randint(1, n)
        if random.random() < 0.05:
            k = random.randint(-5, 0)
        a = [random.randint(-500, 500) for _ in range(n)]
        assert brute_force_sliding_min(a, k) == deque_sliding_min(a, k)
    print("  -> Passed 300 randomized trials.")

if __name__ == "__main__":
    run_tests()
