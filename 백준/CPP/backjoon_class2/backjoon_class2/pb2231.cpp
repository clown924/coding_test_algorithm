#include <iostream>
using namespace std;

int main()
{
	int fractionSum;
	int sum = 0;
	int a, c = 0;
	cin >> fractionSum;

	for (int i = 0; i < fractionSum; i++)
	{
		a = i;
		sum = i;
		while (a)
		{
			sum = sum + a % 10; 
			a = a / 10;  
		}
		if (sum == fractionSum)
		{
			c = i;
			break;
		}
		else
			sum = 0;
	}
	cout << c;
}