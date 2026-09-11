#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "======================================================================"
echo "UMT THEORETICAL COMPETITIVE PROGRAMMING: C++ HARDWARE ASSERTIONS"
echo "======================================================================"

# Compile and run matrix loop tiling
echo "Compiling Cache-Optimized Matrix Loop Tiling..."
g++ -O3 -march=native cpp_matrix_loop_tiling.cpp -o run_matrix
./run_matrix

echo "----------------------------------------------------------------------"
echo "Compiling Branchless Bitmasking..."
g++ -O3 -march=native cpp_branchless_bitmasking.cpp -o run_bitmask
./run_bitmask

echo "----------------------------------------------------------------------"
echo "Compiling In-Place Bit-Reversal FFT..."
g++ -O3 -march=native cpp_inplace_fft.cpp -o run_fft
./run_fft

echo "----------------------------------------------------------------------"
echo "Compiling SIMD-Optimized Fast Zeta Transform..."
g++ -O3 -march=native cpp_fast_zeta_transform.cpp -o run_fzt
./run_fzt

echo "======================================================================"
echo "ALL HARDWARE OPTIMIZED C++ SOLVERS EXECUTED SUCCESSFULLY!"
echo "======================================================================"
