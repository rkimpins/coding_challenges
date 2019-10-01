#include <iostream>
#include <stack>
using namespace std;
/*
 Start with our given point
 use a stack/queue structure
 have a universal visited matrix
 add first point to struct
 while struct !empty or not at point
  take item from struct
  append adjacent movable to positions (not off edge, 1, not visited)
 done dog
 */
bool valid_spot(bool visited[], int X[], int pos)
{
  if (X[pos] && !visited[pos]) {
    return true;
  }
  return false;
}
// N = number of rows, M = number of columns, X = our array
bool connected(int X[], bool visited[], int N, int M, int pos, int tar)
{
  bool found = false;
  int temp = 0;
  int temp2 = 0;
  stack<int> s;
  s.push(pos);
  visited[pos] = true;
  while (!s.empty() && !found) {
    temp = s.top();
    s.pop();

    // add top
    if (temp >= M) {
      temp2 = temp - M;
      if (valid_spot(visited, X, temp2)) {
        if (temp2 == tar) {
          found = true;
        }
        cout << "Adding " << temp2 << endl;
        s.push(temp2);
        visited[temp2] = true;
      }
    }

    // add bot
    if (temp < (N-1)*M) {
      temp2 = temp + M;
      if (valid_spot(visited, X, temp2)) {
        if (temp2 == tar) {
          found = true;
        }
        cout << "Adding " << temp2 << endl;
        s.push(temp2);
        visited[temp2] = true;
      }
    }

    // add right
    if ((temp+1)%M != 0) {
      temp2 = temp + 1;
      if (valid_spot(visited, X, temp2)) {
        if (temp2 == tar) {
          found = true;
        }
        cout << "Adding " << temp2 << endl;
        s.push(temp2);
        visited[temp2] = true;
      }
    }

    // add left
    if (temp%M != 0) {
      temp2 = temp - 1;
      if (valid_spot(visited, X, temp2)) {
        if (temp2 == tar) {
          found = true;
        }
        cout << "Adding " << temp2 << endl;
        s.push(temp2);
        visited[temp2] = true;
      }
    }

  }
  return found;
}

int main()
{
  int X[] = { 
    1, 1, 1, 1, 1, 0, 0, 0, 0, 0,
    1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 
    1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 
    0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 
    0, 0, 1, 1, 1, 1, 1, 1, 1, 1 };
  int N = 5;
  int M = 10;
  bool visited[N*M] = { 0 };
  int pos = 0;
  int tar = 26;
  bool result = connected(X, visited, N, M, pos, tar);
  if (result) {
    cout << "Success";
  } else {
    cout << "Failure";
  }
  cout << endl;
  return 0;
}

