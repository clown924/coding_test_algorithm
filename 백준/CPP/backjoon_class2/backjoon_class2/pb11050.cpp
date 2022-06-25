#include <iostream>
using namespace std;

int factorial(int n)
{
	int result = 1;
	for (int i = n; i > 0; i--)
	{
		result *= i;
	}
	return result;
}

int main()
{
	int n, k;
	int result;

	cin >> n >> k;
	result = factorial(n) / (factorial(k) * factorial(n - k));
	cout << result;
}