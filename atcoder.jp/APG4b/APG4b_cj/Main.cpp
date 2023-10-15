#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;
  
  vector<int> vec(N);
  int sum = 0;
  
  for (int i = 0; i < N; i++) {
    cin >> vec.at(i);
    sum += vec.at(i);
  }
  
  int average = sum / N;
  
  for (int i = 0; i < vec.size(); i++) {
    int num = vec.at(i) - average;
    if (num < 0){
      num = - num;
    }
    cout << num << endl;
  }
}
