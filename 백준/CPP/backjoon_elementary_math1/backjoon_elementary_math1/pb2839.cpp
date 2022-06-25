#include <iostream>
using namespace std;

int main()
{
	int N;
	int count = 0;
	cin >> N;

	if (N % 5 == 0)
		cout << N / 5;

	else
	{
		count = N / 5;
		do
		{
			if ((N - (5 * count)) % 3 == 0)
			{
				cout << count + (N - 5 * count) / 3;
				break;
			}
			count--;
		} while (count >= 0);
	}
	if (count == -1)
		cout << -1;
	return 0;
}