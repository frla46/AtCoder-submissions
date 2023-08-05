#include <bits/stdc++.h>
using ll = long long;
using namespace std;
int main() {
  ll N, M;
  cin >> N >> M;
  ll D[M];
  ll X[M];
  for (ll i = 0; i < M; i++) {
    cin >> X[i];
  }
  sort(X, X + M);
  for (ll i = 1; i < M; i++) {
    D[i - 1] = X[i] - X[i - 1];
  }
  sort(D, D + M);
  ll ret = 0;
  for (ll i = 0; i < M - N; i++) {
    ret += D[i];
  }
  cout << ret;
  return 0;
}
