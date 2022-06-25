#include <iostream>
using namespace std;

int main()
{
	int A, result = 0;
	char num[100];

	cin >> A;
	cin >> num;

	for (int i = 0; i < A; i++)
	{
		result += num[i] - '0';
	}
	cout << result;
	return 0;
}