def cost_w(j, i):
    # Squared interval length (Monge property: (c-a)^2 + (d-b)^2 <= (d-a)^2 + (c-b)^2 is False, but cost (i-j)^2 is convex)
    return (i - j) ** 2

def verify_monge_condition():
    print("[Module 11: Monge Convexity DP] Verifying quadrangle inequality...")
    # Quadrangle condition for submodular convex partition:
    # w(j1, i1) + w(j2, i2) <= w(j1, i2) + w(j2, i1) for j1 < j2 < i1 < i2
    for j1 in range(1, 10):
        for j2 in range(j1 + 1, 15):
            for i1 in range(j2 + 1, 20):
                for i2 in range(i1 + 1, 25):
                    # Monge inequality
                    assert cost_w(j1, i1) + cost_w(j2, i2) <= cost_w(j1, i2) + cost_w(j2, i1)
    print("  -> Quadrangle inequality rigorously verified across discrete coordinate lattice.")

if __name__ == "__main__":
    verify_monge_condition()
