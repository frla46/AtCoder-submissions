#include <algorithm>
#include <bits/stdc++.h>
using ll = long long;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
int main() {
  ll n;
  cin >> n;
  ll a[n];
  ll b[n];
  rep(i, n) cin >> a[i];
  reverse(a, a + n);
  rep(i, n) {
    if (i % 2 == 0) {
      b[i / 2] = a[i];
    } else {
      b[n - i / 2 - 1] = a[i];
    }
  }
  for (ll i : b)
    cout << i << endl;
  return 0;
}
