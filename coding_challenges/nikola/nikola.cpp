#include <iostream>
#include <map>
using namespace std;

/* 
  Problem from Kattis.com
  https://open.kattis.com/contests/e73xfr/problems/nikola
  +---+---+---+---+---+---+
  | 1 | 2 | 3 | 4 | 5 | 6 |
  +---+---+---+---+---+---+
  We have a row of squares
  we can either jump forward and increment our jump size by one
  or jump backwards our jump size without incrementing
  we start by jumping forward 1 square
  each square has a certain cost of landing on it
  ex: to reach N=6, we go 1-2-1-3-6
*/

// e: cost array
// N: size of array
// sum: current summation of costs
// i: current position
// s: current step size
int f(int e[], int N, int sum, int i, int s)
{
  // dynamic map to store calculated results
  static map<pair<int, int>, int> m;
  // if we have already calculated the result, just return it
  if (m[{i, s}]) {
    return m[{i, s}];
  }
  int temp1, temp2;
  // if we are at the last square, end recursion
  if (i == N-1) {
    return sum;
  }
  // if all jumps take us out of array, we are at an invalid branch
  // so return a large value so that this branch isn't considered
  // if there are no possible routes, we expect our result to be large
  if (i-s < 0 && i+s+1 >= N) {
    return 1000000;
  }
  // if we can't jump backwards, jump forwards
  if (i-s < 0) {
    temp1 = f(e, N, sum, i+s+1, s+1);
    m[{i+s+1, s+1}] = temp1; 
    return  e[i+s+1] + temp1;
  }
  // if we can't jump forwards, jump backwards
  if (i+s+1 >= N) {
    temp1 = f(e, N, sum, i-s, s);
    m[{i-s, s}] = temp1; 
    return e[i-s] + temp1;
  }
  // otherwise, recursivly jump forwards and backwards
  temp1 = f(e, N, sum , i-s, s);
  m[{i-s, s}] = temp1; 
  temp2 = f(e, N, sum, i+s+1, s+1);
  m[{i+s+1, s+1}] = temp2; 
  return min(e[i-s] + temp1, e[i+s+1] + temp2);
}

int main()
{
  // get size of array
  int N;
  cin >> N;
  // get cost array
  int e[N];
  for (int i=0; i < N; i++) {
    cin >> e[i];
  }
  // call recursive function to find smallest cost
  cout << f(e, N, e[1], 1, 1);
  return 0;
}
