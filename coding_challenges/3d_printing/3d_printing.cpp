#include <iostream>
using namespace std;

/*
  Imagine we have a 3D printer, and we need to print x statues
  Each printer can either spend a day printing a statue
  or it can print another 3D printer
  What is the minimum number of days needed to print x statues
  This solution works if we assume that it is more efficient to
  have all of our printers doubling until we reach some number, then
  have them all print
  I am ignoring solutions where we have some printers doubling, and 
  some creating statues
  Algorithmn runs in O(log2(x)) time
*/

int min(int x)
{
  int previous = x+2;
  int current = x+1;
  int counter = 0;
  int power = 1;
  while (previous > current) {
    previous = current;
    if (x % power) {
      current = x / power + counter + 1;
    } else {
      current = x / power + counter;
    }
    /*
    cout << "p=" << power;
    cout << " c=" << counter;
    cout << " pre=" << previous;
    cout << " cur=" << current << endl;
    */
    power *= 2;
    counter++;
  }
  /*
  cout << "Number of Printers = " << power/4 << endl;
  cout << "Number of rounds just printing = " << counter-2 << endl;
  cout << "Number of rounds = " << current << endl;
  */
  cout << "Min for " << x << " is " << previous << endl;
  return previous;
}

int main()
{
  min(100);
  return 0;
}

