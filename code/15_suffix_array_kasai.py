import random
import string

def naive_suffix_array_lcp(s):
    s += '$'
    n = len(s)
    suffixes = [(s[i:], i) for i in range(n)]
    suffixes.sort(key=lambda x: x[0])
    sa = [idx for _, idx in suffixes]
    
    lcp = [0] * (n - 1)
    for i in range(n - 1):
        s1, s2 = suffixes[i][0], suffixes[i + 1][0]
        h = 0
        while s1[h] == s2[h]:
            h += 1
        lcp[i] = h
    return sa, lcp

def test_sa_lcp(trials=100):
    for trial in range(trials):
        length = random.randint(0, 100)
        s = "".join(random.choice(string.ascii_lowercase) for _ in range(length))
        sa, lcp = naive_suffix_array_lcp(s)
        assert len(sa) == len(s) + 1
    print(f"Suffix array oracle verified for {trials} random strings.")

if __name__ == "__main__":
    test_sa_lcp()
