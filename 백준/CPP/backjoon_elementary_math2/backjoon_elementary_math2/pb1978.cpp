#include <iostream>
using namespace std;

bool primeNumber(int a);
int main()
{
	int testCase;
	int count = 0;
	cin >> testCase;

	int* arr = new int[testCase];

	for (int i = 0; i < testCase; i++)
	{
		cin >> arr[i];
	}
	for (int j = 0; j < testCase; j++)
	{
		int ATI = arr[j];
		if (primeNumber(ATI) == true)
		{
			count++;
			continue;
		}
		else
			continue;
	}
	cout << count;
	return 0;
}

bool primeNumber(int a)
{
	bool prime = true;
	if (a == 1)
		return false;
	for (int i = 2; i < a; i++)
	{
		if (a % i == 0)
		{
			prime = false;
			break;
		}
		else
		{
			prime = true;
			continue;
		}
	}
	return prime;
}