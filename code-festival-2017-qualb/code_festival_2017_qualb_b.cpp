#include <bits/stdc++.h>
using namespace std;
int main() {
  int N;
  cin >> N;
  map<int, int> cnt;
  for (int i = 0; i < N; i++) {
    int j;
    cin >> j;
    cnt[j]++;
  }
  int M;
  cin >> M;
  for (int i = 0; i < M; i++) {
    int j;
    cin >> j;
    if (cnt[j]) {
      cnt[j]--;
    } else {
      cout << "NO";
      return 0;
    }
  }
  cout << "YES";
  return 0;
}
