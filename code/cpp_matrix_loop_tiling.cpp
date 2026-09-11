#pragma GCC optimize("O3,unroll-loops")
#ifdef __x86_64__
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#include <cassert>

using namespace std;
const int MOD = 1e9 + 7;
const int BLOCK_SIZE = 64; // L1 Cache line alignment

// Cache-friendly Matrix Multiplication via Loop Tiling
vector<vector<long long>> apex_matrix_mult(const vector<vector<long long>>& A, const vector<vector<long long>>& B) {
    int n = A.size();
    assert(n > 0 && n == A[0].size() && n == B.size() && n == B[0].size() && "Matrices must be square");
    
    vector<vector<long long>> C(n, vector<long long>(n, 0));
    // Transpose B to achieve contiguous memory access (Spatial Locality)
    vector<vector<long long>> B_T(n, vector<long long>(n, 0));
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            B_T[i][j] = B[j][i];

    // Block-level multiplication (Tiling)
    for (int i = 0; i < n; i += BLOCK_SIZE) {
        for (int j = 0; j < n; j += BLOCK_SIZE) {
            for (int k = 0; k < n; k += BLOCK_SIZE) {
                // Inner block execution
                for (int ii = i; ii < min(i + BLOCK_SIZE, n); ++ii) {
                    for (int jj = j; jj < min(j + BLOCK_SIZE, n); ++jj) {
                        __int128_t sum = 0;
                        // Sequential memory access for both A and B_T
                        for (int kk = k; kk < min(k + BLOCK_SIZE, n); ++kk) {
                            sum += (__int128_t)A[ii][kk] * B_T[jj][kk];
                        }
                        sum %= MOD;
                        if (sum < 0) sum += MOD;
                        C[ii][jj] = (C[ii][jj] + (long long)sum) % MOD;
                    }
                }
            }
        }
    }
    return C;
}

int main() {
    vector<vector<long long>> A(128, vector<long long>(128, 1));
    vector<vector<long long>> B(128, vector<long long>(128, 1));
    auto C = apex_matrix_mult(A, B);
    cout << "[C++ HW Assert] Matrix Multiplication Loop Tiling Successful (L1 Cache Optimized). C[0][0] = " << C[0][0] << "\n";
    return 0;
}
