import random

def check(t, k, P):
    return sum(t // x for x in k) >= P

def binary_search_schedule(k, P):
    if not k:
        return 0 if P == 0 else -1
    low, high = 0, P * max(k)
    ans = high
    while low <= high:
        mid = (low + high) // 2
        if check(mid, k, P):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def run_tests():
    print("[Module 04: Binary Search on Answer] Validating monotonic predicate scheduling...")
    k = [2, 3, 7]
    P = 8
    ans = binary_search_schedule(k, P)
    assert ans == 9 # at t=8: 8//2 + 8//3 + 8//7 = 4 + 2 + 1 = 7 (not enough), at t=8 sum is 7. Wait, at t=9: 4+3+1=8.
    assert check(ans, k, P) and not check(ans - 1, k, P)
    print("  -> Passed boundary check with exact precision.")

if __name__ == "__main__":
    run_tests()
