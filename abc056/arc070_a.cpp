#include <bits/stdc++.h>
using ll = long long;
#define rep(i, n) for (int i = 0; (i) < (n); ++(i))
using namespace std;
int main() {
  ll x = 0;
  cin >> x;
  int i = 0;
  while (x > 0) {
    x -= ++i;
  }
  cout << i;
  return 0;
}