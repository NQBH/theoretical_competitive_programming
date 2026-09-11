import random



class LazySegmentTree:
    def __init__(self, n):
        self.tree_sum = [0] * (4 * n + 1)
        self.lazy = [0] * (4 * n + 1)
    
    def push_down(self, node, l, r):
        if self.lazy[node] == 0:
            return
        mid = (l + r) // 2
        self.tree_sum[2 * node] += self.lazy[node] * (mid - l + 1)
        self.lazy[2 * node] += self.lazy[node]
        self.tree_sum[2 * node + 1] += self.lazy[node] * (r - mid)
        self.lazy[2 * node + 1] += self.lazy[node]
        self.lazy[node] = 0

    def update_range(self, node, l, r, ql, qr, v):
        if ql <= l and r <= qr:
            self.tree_sum[node] += v * (r - l + 1)
            self.lazy[node] += v
            return
        self.push_down(node, l, r)
        mid = (l + r) // 2
        if ql <= mid:
            self.update_range(2 * node, l, mid, ql, qr, v)
        if qr > mid:
            self.update_range(2 * node + 1, mid + 1, r, ql, qr, v)
        self.tree_sum[node] = self.tree_sum[2 * node] + self.tree_sum[2 * node + 1]

    def query_range(self, node, l, r, ql, qr):
        if ql <= l and r <= qr:
            return self.tree_sum[node]
        self.push_down(node, l, r)
        mid = (l + r) // 2
        res = 0
        if ql <= mid:
            res += self.query_range(2 * node, l, mid, ql, qr)
        if qr > mid:
            res += self.query_range(2 * node + 1, mid + 1, r, ql, qr)
        return res

def stress_test():
    n = 1000
    tree = LazySegmentTree(n)
    a = [0] * n
    
    for _ in range(500):
        op = random.choice(['update', 'query'])
        ql = random.randint(0, n - 1)
        qr = random.randint(ql, n - 1)
        if op == 'update':
            v = random.randint(1, 100)
            tree.update_range(1, 0, n - 1, ql, qr, v)
            for i in range(ql, qr + 1):
                a[i] += v
        else:
            ans_tree = tree.query_range(1, 0, n - 1, ql, qr)
            ans_naive = sum(a[ql:qr + 1])
            assert ans_tree == ans_naive, "Mismatch found!"
    print("Lazy Segment Tree passed stress testing.")

if __name__ == "__main__":
    stress_test()
