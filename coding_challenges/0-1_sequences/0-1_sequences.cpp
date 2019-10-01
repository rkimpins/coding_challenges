#include <iostream>
using namespace std;

int inversions(char X[], int N)
{
  int result = 0, intermediate = 0, hweight = 0;
  for (int i=0; i < N; i++) {
    // cout << (int) X[i];
    if (X[i]) {
      hweight++;
    }
  }
  hweight--;
  for (int i=0; i < N; i++) {
    if (X[i]) {
      intermediate += (N - i - 1 - hweight--);
    } else {
      result += intermediate;
      intermediate = 0;
    }
  }
  // cout << " result=" << result << endl;
  return result;
}

int sum_inversions(char X[], int N)
{
  int marks = 0;
  int result = 0;
  char Y[N];
  for (int i=0; i < N; i++) {
    if (X[i] == '?') {
      marks++;
    }
  }
  for (int i=0; i < (2 << (marks-1)); i++) {
    int temp_i = i;
    for (int j=N-1; j >= 0; j--) {
      if (X[j] == '?') {
        Y[j] = (char) (temp_i % 2);
        temp_i /= 2;
      } else {
        Y[j] = X[j];
      }
    }
    result += inversions(Y, N);
  }
  return result;
}


int main()
{
  int test = -1;
  // Test 1
  if (test == 1 || test == -1) {
    char X[] = { '?', 0, '?' };
    int N = sizeof(X)/sizeof(X[0]);
    cout << "?0? " << 
      "Expected:" << "3 Result:" << sum_inversions(X, N) << endl;
  }
  // Test 2
  if (test == 2 || test == -1) {
    char X[] = { '?', 1, '?' };
    int N = sizeof(X)/sizeof(X[0]);
    cout << "?1? " << 
      "Expected:" << "3 Result:" << sum_inversions(X, N) << endl;
  }
  // Test 3
  if (test == 3 || test == -1) {
    char X[] = { '?', 1, '?', 0 };
    int N = sizeof(X)/sizeof(X[0]);
    cout << "?1?0 " << 
      "Expected:" << "11 Result:" << sum_inversions(X, N) << endl;
  }
  // Test 4
  if (test == 4 || test == -1) {
    char X[] = { '?', '?', '?', '?', '?', '?', '?', '?' };
    int N = sizeof(X)/sizeof(X[0]);
    cout << "???????? " << 
      "Expected:" << "1792 Result:" << sum_inversions(X, N) << endl;
  }
  return 0;
}
