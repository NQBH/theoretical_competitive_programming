def nim_game_winner(piles):
    xor_sum = 0
    for x in piles:
        xor_sum ^= x
    return "First" if xor_sum != 0 else "Second"

def run_tests():
    print("[Module 12: Game Theory & Geometry] Validating Bouton's Nim Theorem...")
    assert nim_game_winner([3, 4, 5]) == "First" # 3 ^ 4 ^ 5 = 2 != 0
    assert nim_game_winner([1, 2, 3]) == "Second" # 1 ^ 2 ^ 3 = 0
    print("  -> Passed Bouton Galois Field XOR Game invariants.")

if __name__ == "__main__":
    run_tests()
