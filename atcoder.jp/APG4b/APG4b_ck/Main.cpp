#include <bits/stdc++.h>
using namespace std;

int main() {
  string S;
  cin >> S;

  // ここにプログラムを追記
  int num_plus = 0, num_minus = 0;
  char c;
  for (int i = 0; i < S.size(); i++) {
    c = S.at(i);
    if (c == '+') {
      num_plus ++;
    }
    else if (c == '-') {
      num_minus ++;
    }
  }
  cout << 1 + num_plus - num_minus << endl;
}
