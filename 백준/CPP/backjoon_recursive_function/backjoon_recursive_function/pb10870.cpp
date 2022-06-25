#include <iostream>
using namespace std;
int Fibonacci(int num);
int main()
{
	int N;
	cin >> N;

	cout << Fibonacci(N);
}

int Fibonacci(int num)
{
	if (num == 0)
		return 0;
	else if (num == 1)
		return 1;
	else
		return Fibonacci(num - 1) + Fibonacci(num - 2);
}