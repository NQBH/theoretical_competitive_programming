import random

def evaluate_3sat_brute_force(clauses, num_vars):
    # Oracle: 3-SAT Exponential Brute Force Evaluator by branching on all possible truth assignments
    for i in range(1 << num_vars):
        assignment = [(i >> j) & 1 for j in range(num_vars)]
        valid = True
        for clause in clauses:
            clause_valid = False
            for lit in clause:
                var_idx = abs(lit) - 1
                val = assignment[var_idx] if lit > 0 else 1 - assignment[var_idx]
                if val:
                    clause_valid = True
                    break
            if not clause_valid:
                valid = False
                break
        if valid:
            return True
    return False

def test_np_hard(trials=100):
    sat_count = 0
    unsat_count = 0
    for trial in range(trials):
        num_vars = random.randint(3, 10)
        num_clauses = random.randint(5, 20)
        clauses = []
        for _ in range(num_clauses):
            clause = []
            vars_sampled = random.sample(range(1, num_vars + 1), 3)
            for var in vars_sampled:
                if random.choice([True, False]):
                    var = -var
                clause.append(var)
            clauses.append(clause)
        is_sat = evaluate_3sat_brute_force(clauses, num_vars)
        if is_sat:
            sat_count += 1
        else:
            unsat_count += 1
    print(f"3-SAT Exponential Brute Force Evaluator finished {trials} trials.")
    print(f"Satisfiable: {sat_count}, Unsatisfiable: {unsat_count}")

if __name__ == "__main__":
    test_np_hard()
