#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

vector<vector<int>> patience_sorting_partitions(const vector<int>& a) {
    vector<vector<int>> piles;
    for (int x : a) {
        auto it = lower_bound(piles.begin(), piles.end(), x, [](const vector<int>& p, int val) {
            return p.back() < val;
        });
        if (it == piles.end()) piles.push_back({x});
        else it->push_back(x);
    }
    return piles;
}

int main() {
    vector<int> a = {4, 2, 5, 3};
    auto piles = patience_sorting_partitions(a);
    for (auto p : piles) {
        for (int x : p) cout << x << " ";
        cout << endl;
    }
    return 0;
}
