#include <iostream>
using namespace std;

void average(int num)
{
	double result = 0;
	double count = 0;
	double percent;
	double* student = new double[num];
	for (int i = 0; i < num; i++)
	{
		cin >> student[i];
		result += student[i];
	}
	result = result / (double)num;
	
	for (int i = 0; i < num; i++)
	{
		if (student[i] > result)
			count++;
	}
	percent = count / (double)num * 100;
	cout << fixed;
	cout.precision(3);
	cout << (double)percent << "%\n";
}

int main()
{
	int testCase;
	int num;
	cin >> testCase;

	for (int i = 0; i < testCase; i++)
	{
		cin >> num;
		average(num);
	}
	return 0;
}