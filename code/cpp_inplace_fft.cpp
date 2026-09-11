#pragma GCC optimize("O3,unroll-loops")
#ifdef __x86_64__
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#include <iostream>
#include <vector>
#include <complex>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <utility>

using namespace std;
typedef complex<double> cd;
const double PI = acos(-1);

// In-Place Iterative FFT
void apex_fft(vector<cd>& a, bool invert) {
    int n = a.size();
    assert((n & (n - 1)) == 0); // Array size must be a power of 2
    
    // 1. Bit-Reversal Permutation
    for (int i = 1, j = 0; i < n; i++) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) swap(a[i], a[j]);
    }
    
    // 2. Iterative Bottom-Up Merging (Eliminates O(N) recursive overhead)
    for (int len = 2; len <= n; len <<= 1) {
        double angle = 2 * PI / len * (invert ? -1 : 1);
        
        for (int j = 0; j < len / 2; j++) {
            cd w = std::polar(1.0, angle * j);
            for (int i = 0; i < n; i += len) {
                // Butterfly Operation
                cd u = a[i + j], v = a[i + j + len / 2] * w;
                a[i + j] = u + v;
                a[i + j + len / 2] = u - v;
            }
        }
    }
    
    // Normalization for Inverse FFT
    if (invert) {
        for (cd & x : a) x /= n;
    }
}

int main() {
    vector<cd> a = {cd(1,0), cd(2,0), cd(3,0), cd(4,0)};
    apex_fft(a, false);
    cout << "[C++ HW Assert] In-Place Bit-Reversal FFT computed. a[0] = " << a[0].real() << "\n";
    return 0;
}
