#include <map>
#include <iostream>
using namespace std;


int fib(int x) {
  static map<int, int> m;
  if (m[x]) {
    return m[x];
  }
  if (x == 1) {
    return 0;
  }
  if (x == 2) {
    return 1;
  }
  int temp1, temp2;
  temp1 = fib(x-2);
  m[x-2] = temp1;
  temp2 = fib(x-1);
  m[x-1] = temp2;
  return temp1 + temp2;
}



int main()
{
  for (int i=1; i < 48; i++) {
    cout << fib(i) << endl;;
  }
  return 0;
}
