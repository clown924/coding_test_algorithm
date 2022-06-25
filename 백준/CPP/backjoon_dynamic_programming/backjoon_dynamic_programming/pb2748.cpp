#include <iostream>
using namespace std;

long long int d[100];
long long int Fibonacci(long long int N);

int main()
{
	long long int N;
	cin >> N;

	cout << Fibonacci(N);
}

long long int Fibonacci(long long int N)
{
	if (N == 0)
		return 0;

	if (N == 1)
		return 1;

	if (d[N] != 0)
		return d[N];

	return d[N] = Fibonacci(N - 1) + Fibonacci(N - 2);  // memoization
}