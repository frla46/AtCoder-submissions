#include <algorithm>
#include <bits/stdc++.h>
using namespace std;
int main() {
  int N;
  cin >> N;
  vector<int> h(N);
  for (int i = 0; i < N; i++) {
    int j;
    cin >> j;
    h[i] = j;
  }
  int cnt = 0;
  bool flg = false;
  while (true) {
    for (int i = 0; i < N; i++) {
      if (h[i] != 0) {
        flg = true;
        h[i] -= 1;
      } else if (flg && h[i] == 0) {
        flg = false;
        cnt += 1;
      }
    }
    if (flg) {
      flg = false;
      cnt += 1;
    }
    if (all_of(h.begin(), h.end(), [](int i) { return i == 0; }))
      break;
  }
  cout << cnt;
  return 0;
}
