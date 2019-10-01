#include <iostream>
#include <map>
#include <set>
using namespace std;

/*
 * Problem from Kattis.com
 * https://open.kattis.com/contests/e73xfr/problems/eatingeverything
 * Imagine we are going from stand to stand, eating pizza
 * the stands are connected by 1 way paths, without loops
 * At each stand, we may choose to eat a pizza or not
 * we start by eating 1 pizza, then a half, then a fourth, 1/2^k
 * for a given route, our satisfaction is 
 * stands_satisfaction * fraction of pizza eaten
 */

// pos: current position of stand
// sat_values: the level of satisfaction from each stand
// routes: all possible routes we can take from a given stand
double max_satisfaction(int pos, int sat_values[], map<int, set<int>> routes)
{
  // store already calculated results here
  static map<int, double> dyno_map;
  // if value has already been calculated, return that value
  if (dyno_map[pos]) {
    return dyno_map[pos];
  }
  // if there are no more routes to take, return final position
  if (routes[pos].empty()) {
    dyno_map[pos] = sat_values[pos];
    return sat_values[pos];
  }
  // of all possible routes, calculate the best one recursively
  double maximum = 0;
  double temp;
  for (auto route : routes[pos]) {
    temp = max_satisfaction(route, sat_values, routes);
    dyno_map[route] = temp; // save solution
    if (temp > maximum) {
      maximum = temp;
    }
  }
  // calculate if it is better to take current satisfaction value
  return max(sat_values[pos] + 0.5 * maximum, maximum);
}

int main()
{
  // get number of stands
  int nstands;
  cin >> nstands;
  // get number of paths
  int npaths;
  cin >> npaths;
  int sat_values[nstands];
  map<int, set<int>> routes; 
  // represent stand 0 connecting to every other stand
  for (int i=1; i < nstands; i++) {
    routes[0].insert(i);
  }
  // get satisfaction values
  for (int i=0; i < nstands; i++) {
    cin >> sat_values[i];
  }
  // get possible paths
  int start, end;
  for (int i=0; i < npaths; i++) {
    cin >> start >> end;
    routes[start].insert(end);
  }
  // call recursive function to find optimal satisfaction path
  cout << max_satisfaction(0, sat_values, routes);
  return 0;
}
/* 
  SAMPLE INPUTS
  5 5
  1 4 6 2 100
  0 1
  1 2
  0 3
  2 4
  3 4
  >>100
 
  3 2
  1 0 1
  0 1
  1 2
  >>1.5
 
  3 2
  3 2 1
  0 1
  1 2
  >>4.25
*/
