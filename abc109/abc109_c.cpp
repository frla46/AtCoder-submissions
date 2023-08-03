#include <bits/stdc++.h>
using namespace std;
template <typename T> inline bool chmax(T &a, const T &b) {
  bool compare = a < b;
  if (a < b)
    a = b;
  return compare;
}
int main() {
  int N, X;
  cin >> N >> X;
  vector<int> x(N);
  for (int i = 0; i < N; i++) {
    int j;
    cin >> j;
    x[i] = max(X - j, j - X);
  }
  int ret = x[0];
  for (int i : x) {
    ret = gcd(ret, i);
  }
  cout << ret;
  return 0;
}
