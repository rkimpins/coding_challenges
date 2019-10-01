#include <iostream>
using namespace std;

int main() {
  int N, M;
  for(;;) {
    cin >> N >> M;
    if (N == 0 && M == 0) {
      break;
    }
    int A[N];
    int B[M];

    for (int i=0; i < N; i++) {
      cin >> A[i];
    }
    for (int i=0; i < M; i++) {
      cin >> B[i];
    }

    int i = 0, j = 0, result = 0;
    while(i < N && j < M) {
      // cout << "i:" << i << " j:" << j << endl;
      if (A[i] == B[j]) {
        result++; i++; j++;
      } else if (A[i] > B[j]) {
        j++;
      } else {
        i++;
      }
    }
    cout << result << endl;
  }
  return 0;
}
