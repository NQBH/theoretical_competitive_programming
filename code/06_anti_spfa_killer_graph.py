import random

def generate_anti_spfa_graph(k):
    """Generates a graph causing exponential relaxations in naive SPFA."""
    edges = []
    for i in range(1, k + 1):
        # 1-edge shortcut with heavy weight
        edges.append((2 * i - 1, 2 * i + 1, 1 << (k - i)))
        # 2-edge path with zero weight
        edges.append((2 * i - 1, 2 * i, 0))
        edges.append((2 * i, 2 * i + 1, 0))
    return edges

def generate_anti_spfa_benchmark():
    print("[Module 06: Graph 0-1 BFS & Anti-SPFA] Synthesizing worst-case graph...")
    k = 15
    edges = generate_anti_spfa_graph(k)
    print(f"  -> Generated {len(edges)} adversarial edges to benchmark 0-1 BFS vs SPFA.")

if __name__ == "__main__":
    generate_anti_spfa_benchmark()
