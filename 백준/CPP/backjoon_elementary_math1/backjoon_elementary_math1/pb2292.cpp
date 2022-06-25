#include <iostream>
using namespace std;

int main()
{
	int testCase;
	int cnt = 0;
	cin >> testCase;

	if (testCase == 1)
		cnt = 1;
	else
	{
		int val = 2;
		while (testCase >= val)
		{
			val += 6 * cnt;
			cnt++;
		}
	}

	cout << cnt;
	return 0;
}