#include <bits/stdc++.h>
using namespace std;
int main()
{
  int A[] = { 1, 2, 3, 3, 3, 5, 8 };
  const int N = sizeof(A) / sizeof(int);

  for (int i = 1; i <= 10; ++i) {
    int* p = lower_bound(A, A + N, i);
    int* p = upper_bound(A, A + N, i);
    cout << "Searching for " << i << ".  ";
    cout << "Result: index = " << p - A << ", ";
    if (p != A + N)
      cout << "A[" << p - A << "] == " << *p << endl;
    else
      cout << "which is off-the-end." << endl;
  }
}
























//google i talee 1536427 Abd.jalil.921 i taleem i taleem fb abd.jalil.165 abd&jalil921 `italeem
