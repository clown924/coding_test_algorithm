#include <iostream>
using namespace std;

int main()
{
	int B[10];
	int testCase;

	cin >> testCase;
	for (int i = 0; i < testCase; i++)
	{
		string A;
		cin >> A;

		int count = 0;
		int result = 0;

		for (int j = 0; j < A.length(); j++)
		{
			if (A[j] == 'O')
			{
				count++;
				result += count;
			}
			else
				count = 0;
		}
		cout << result << endl;
	}
	return 0;
}