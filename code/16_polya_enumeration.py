import random
import itertools
import sympy

def polya_necklaces_sympy(n, c):
    # SymPy computer algebra reference oracle (exact symbolic arithmetic)
    ans = sum(int(sympy.totient(n // d)) * (c ** d) for d in range(1, n + 1) if n % d == 0)
    return ans // n

def brute_force_necklaces(n, c):
    # Oracle: Generates all states and filters by cyclic equivalents
    unique_configurations = set()
    for current in itertools.product(range(c), repeat=n):
        min_rep = current
        for shift in range(1, n):
            rotated = current[shift:] + current[:shift]
            if rotated < min_rep:
                min_rep = rotated
        unique_configurations.add(min_rep)
    return len(unique_configurations)

def euler_phi(n):
    res = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
            res -= res // i
        i += 1
    if n > 1:
        res -= res // n
    return res

def polya_necklaces(n, c, mod):
    ans = 0
    d = 1
    while d * d <= n:
        if n % d == 0:
            ans = (ans + ((euler_phi(n // d) % mod) * pow(c, d, mod)) % mod) % mod
            if d * d != n:
                ans = (ans + ((euler_phi(d) % mod) * pow(c, n // d, mod)) % mod) % mod
        d += 1
    return (ans * pow(n, -1, mod)) % mod

def run_fuzzer(trials=100):
    mod = 10**9 + 7
    for _ in range(trials):
        n = random.randint(1, 10)
        c = random.randint(1, 4)
        sym = polya_necklaces_sympy(n, c) % mod
        opt = polya_necklaces(n, c, mod)
        assert sym == opt, f"SymPy vs Opt mismatch for N={n}, C={c}: sym={sym}, opt={opt}"
        if c ** n <= 30000:
            bf = brute_force_necklaces(n, c) % mod
            assert bf == opt, f"Brute force mismatch for N={n}, C={c}: bf={bf}, opt={opt}"
    print(f"Polya enumeration verified against {trials} random trials (including SymPy oracle).")

if __name__ == "__main__":
    run_fuzzer()
