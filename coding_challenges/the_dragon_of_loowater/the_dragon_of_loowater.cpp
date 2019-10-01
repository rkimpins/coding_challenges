/* 
 * Source: https://open.kattis.com/problems/loowater
 * Author: Randal Kimpinski
 * Completed: Feb 20, 2019
 */

#include <iostream>
using namespace std;

/* Print an array */
void printArray(int arr[], int size)
{
  int i;
  for (i=0; i < size; i++) {
    cout << arr[i] << " ";
  }
  cout << endl;
}

/* Utility swap function */
void swap(int* a, int* b) 
{ 
  int t = *a; 
  *a = *b; 
  *b = t; 
} 

/* This function takes last element as pivot, places 
 * the pivot element at its correct position in sorted 
 * array, and places all smaller (smaller than pivot) 
 * to left of pivot and all greater elements to right 
 * of pivot */
int partition (int arr[], int low, int high) 
{ 
  int pivot = arr[high];    // pivot 
  int i = (low - 1);  // Index of smaller element 

  for (int j = low; j <= high- 1; j++) 
  { 
    // If current element is smaller than or 
    // equal to pivot 
    if (arr[j] <= pivot) 
    { 
      i++;    // increment index of smaller element 
      swap(&arr[i], &arr[j]); 
    } 
  } 
  swap(&arr[i + 1], &arr[high]); 
  return (i + 1); 
} 
  
/* The main function that implements QuickSort 
 * arr[] --> Array to be sorted, 
 * low  --> Starting index, 
 * high  --> Ending index */
void quickSort(int arr[], int low, int high) 
{ 
  if (low < high) 
  { 
    /* pi is partitioning index, arr[p] is now 
     * at right place */
    int pi = partition(arr, low, high); 

    /* Separately sort elements before 
     * partition and after partition */
    quickSort(arr, low, pi - 1); 
    quickSort(arr, pi + 1, high); 
  } 
} 

int main() {
  // number of heads, number of knights, total cost, placholders 1 and 2
  int N, M, sum, i, j;
  // diameter of heads, height of knights
  int heads[20000];
  int knights[20000];
  cin >> N >> M;

  while (N != 0 || M != 0) {
    // Array of head heights and knight heights
    // Fill arrays from input (unsorted)
    for (int i=0; i < N; i++) {
      cin >> heads[i];
    }
    for (int i=0; i < M; i++) {
      cin >> knights[i];
    }

    // sort our arrays
    quickSort(heads, 0, N-1);
    quickSort(knights, 0, M-1);

    // Initialize counters
    sum = 0;
    i = 0;
    j = 0;
    /* This loop matches each knight with a head.
     * Since we start from the minimum of each, and increment the
     * knights when one isn't tall enough, we assign the smallest
     * possible knight to cut each head.
     * If we have enough knights which are tall enough, then we will
     * have incremented i through the entire array.
     * In the case that we don't have enough knights, or tall enough
     * knights, we exit */
    while (i < N && j < M) {
      if (heads[i] > knights[j]) {
        j++;
      } else if (heads[i] <= knights[j]) {
        sum += knights[j];
        i++;
        j++;
      }
    }
    /* If we got to the end of our heads array,
      then we found a knight for each head */
    if (i >= N) {
      cout << sum << endl;
    } else {
      cout << "Loowater is doomed!" << endl;
    }
    // Initialize N and M for start of loop
    cin >> N >> M;
  }
  return 0;
}
