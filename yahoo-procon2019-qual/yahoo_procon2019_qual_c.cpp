#include <bits/stdc++.h>
using ll = long long;
using namespace std;
int main() {
  ll K, A, B;
  cin >> K >> A >> B;
  ll cnt;
  if (B - A > 2) {
    int change = ((K - A + 1) / 2 > 0 ? (K - A + 1) / 2 : 0);
    cnt = change * (B - A) + K - change * 2 + 1;
  } else {
    cnt = K + 1;
  }
  cout << cnt;
  return 0;
}
