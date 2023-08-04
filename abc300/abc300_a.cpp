#include <bits/stdc++.h>
using ll = long long;
using namespace std;
int main() {
  ll N, A, B;
  cin >> N >> A >> B;
  for (ll i = 1; i <= N; i++) {
    ll j;
    cin >> j;
    if (j == A + B) {
      cout << i;
      return 0;
    }
  }
  return 0;
}
