#pragma GCC optimize("O3")
#ifdef __x86_64__
#pragma GCC target("bmi,bmi2,lzcnt,popcnt")
#endif
#include <iostream>
#include <algorithm>
#include <utility>

using namespace std;
long long apex_valid_configs = 0;
int ALL_ONES;

// Execute backtracking
void apex_solve(int row_mask, int ld_mask, int rd_mask) {
    if (row_mask == ALL_ONES) {
        apex_valid_configs++;
        return;
    }
    // Isolate valid bit positions
    int valid_positions = ALL_ONES & ~(row_mask | ld_mask | rd_mask);
    
    // Iterate via bit manipulation
    while (valid_positions) {
        // Extract least significant valid bit using 2's complement
        int p = valid_positions & -valid_positions;
        valid_positions ^= p; // Fast bit toggle
        
        // Tail recursion heavily optimized by compiler
        apex_solve(row_mask | p, (ld_mask | p) << 1, (rd_mask | p) >> 1);
    }
}

long long get_n_queens_apex(int n) {
    ALL_ONES = (1 << n) - 1;
    apex_valid_configs = 0;
    apex_solve(0, 0, 0);
    return apex_valid_configs;
}

int main() {
    int n = 8;
    cout << "[C++ HW Assert] N-Queens Branchless Bitmasking via CPU Intrinsics (N=" << n << "): " << get_n_queens_apex(n) << " configs.\n";
    return 0;
}
