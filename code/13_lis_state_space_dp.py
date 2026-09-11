import random
import bisect

def get_lis(a):
    m = []
    for x in a:
        pos = bisect.bisect_left(m, x)
        if pos == len(m):
            m.append(x)
        else:
            m[pos] = x
    return len(m)

def min_non_increasing_partition(a):
    partitions = []
    for x in a:
        placed = False
        for p in partitions:
            if p[-1] >= x:
                p.append(x)
                placed = True
                break
        if not placed:
            partitions.append([x])
    return len(partitions)

def run_fuzzer(trials=1000):
    for trial in range(trials):
        n = random.randint(1, 100)
        a = [random.randint(1, 1000) for _ in range(n)]
        lis = get_lis(a)
        non_increasing_cov = min_non_increasing_partition(a)
        assert lis == non_increasing_cov, f"Mirsky's Theorem failed on {a}"
    print(f"Verified Mirsky's Theorem for {trials} random arrays.")

if __name__ == "__main__":
    run_fuzzer()
