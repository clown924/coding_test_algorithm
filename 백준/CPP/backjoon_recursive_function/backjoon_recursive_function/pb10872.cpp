#include <iostream>
using namespace std;
int factorial(int num);
int main()
{
	int N;
	cin >> N;

	cout << factorial(N);
}

int factorial(int num)
{
	if (num == 0)
		return 1;
	else
		return num * factorial(num - 1);
	
}