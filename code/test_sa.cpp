#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<int> build_suffix_array(string s) {
 s += char(0);
 int n = s.size();
 vector<int> p(n), c(n), cnt(max(256, n), 0);
 for (int i = 0; i < n; i++) cnt[(unsigned char)s[i]]++;
 for (int i = 1; i < 256; i++) cnt[i] += cnt[i - 1];
 for (int i = 0; i < n; i++) p[--cnt[(unsigned char)s[i]]] = i;
 
 c[p[0]] = 0;
 int classes = 1;
 for (int i = 1; i < n; i++) {
 if (s[p[i]] != s[p[i - 1]]) classes++;
 c[p[i]] = classes - 1;
 }
 
 vector<int> pn(n), cn(n);
 for (int h = 0; (1 << h) < n; ++h) {
 for (int i = 0; i < n; i++) {
 pn[i] = p[i] - (1 << h);
 if (pn[i] < 0) pn[i] += n;
 }
 fill(cnt.begin(), cnt.begin() + classes, 0);
 for (int i = 0; i < n; i++) cnt[c[pn[i]]]++;
 for (int i = 1; i < classes; i++) cnt[i] += cnt[i - 1];
 for (int i = n - 1; i >= 0; i--) p[--cnt[c[pn[i]]]] = pn[i];
 
 cn[p[0]] = 0;
 classes = 1;
 for (int i = 1; i < n; i++) {
 pair<int, int> cur = {c[p[i]], c[(p[i] + (1 << h)) % n]};
 pair<int, int> prev = {c[p[i - 1]], c[(p[i - 1] + (1 << h)) % n]};
 if (cur != prev) ++classes;
 cn[p[i]] = classes - 1;
 }
 c = cn;
 if (classes == n) break;
 }
 return p;
}

vector<int> build_lcp(string s, const vector<int>& p) {
 s += char(0);
 int n = s.size();
 vector<int> rank(n);
 for (int i = 0; i < n; i++) rank[p[i]] = i;
 
 vector<int> lcp(n - 1, 0);
 int h = 0;
 for (int i = 0; i < n; i++) {
 if (rank[i] > 0) {
 int j = p[rank[i] - 1];
 while (i + h < n && j + h < n && s[i + h] == s[j + h]) h++;
 lcp[rank[i] - 1] = h;
 if (h > 0) h--;
 }
 }
 return lcp;
}

int main() {
    string s = "ababba";
    vector<int> p = build_suffix_array(s);
    vector<int> lcp = build_lcp(s, p);
    cout << "SA:"; for(int x : p) cout << " " << x; cout << endl;
    cout << "LCP:"; for(int x : lcp) cout << " " << x; cout << endl;
    return 0;
}
