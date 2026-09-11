import os
import subprocess
import sys
import time

modules = [
    "01_two_pointers_stress_test.py",
    "02_sliding_window_fuzzer.py",
    "03_prefix_diff_2d_validator.py",
    "04_binary_search_schedule.py",
    "05_rollback_dsu_oracle.py",
    "06_anti_spfa_killer_graph.py",
    "07_tree_lca_euler_tour.py",
    "08_sos_dp_hypercube.py",
    "09_matrix_min_plus_power.py",
    "10_lazy_segment_tree_fuzzer.py",
    "11_monge_dnc_optimizer.py",
    "12_nim_game_geometry_hull.py",
    "13_lis_state_space_dp.py",
    "14_network_flow_dinic.py",
    "15_suffix_array_kasai.py",
    "16_polya_enumeration.py",
    "17_tree_dp_ida_star.py",
    "18_np_hard_bitmask_dp.py",
]

def main():
    print("=" * 70)
    print("UMT THEORETICAL COMPETITIVE PROGRAMMING: 18-MODULE TEST HARNESS")
    print("=" * 70)
    start_all = time.time()
    for mod in modules:
        script_path = os.path.join(os.path.dirname(__file__), mod)
        res = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
        if res.returncode != 0:
            print(f"FAILED: {mod}\n{res.stderr}")
            sys.exit(1)
        else:
            print(res.stdout.strip())
    total_time = time.time() - start_all
    print("=" * 70)
    print(f"ALL 18 MODULES VERIFIED SUCCESSFULLY (Total Time: {total_time:.3f}s)")
    print("=" * 70)

if __name__ == "__main__":
    main()
