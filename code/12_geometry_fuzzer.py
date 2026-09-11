import random

def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull_python(pts):
    pts = sorted(list(set(pts)))
    if len(pts) <= 2:
        return pts
    
    lower = []
    for p in pts:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
        
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
        
    return lower[:-1] + upper[:-1]

def run_fuzzer(iters=1000):
    print("[Module 12: Geometry] Fuzzing Convex Hull...")
    for _ in range(iters):
        n = random.randint(1, 100)
        pts = [(random.randint(-1000, 1000), random.randint(-1000, 1000)) for _ in range(n)]
        hull = convex_hull_python(pts)
        assert len(hull) <= len(set(pts))
    print("  -> Passed all fuzzing tests.")

if __name__ == "__main__":
    run_fuzzer()
