#include <iostream>
using namespace std;

int main()
{
	int M, N;
	int sum = 0;
	int check = 0;
	cin >> M >> N;

	int min = 10000;
	if (M == 1)
		M++;
	for (int j = M; j <= N; j++)
	{
		if (j == 2)
		{
			check = 1;
			goto C;
		}
		for (int i = 2; i < j; i++)
		{
			if (j % i == 0)
			{
				
				check = 0;
				break;
			}
			else
			{
				check = 1;
				continue;
			}
		}
		C:if (check == 1)
		{
			sum += j;
			if (j < min)
				min = j;
		}
	}
	if (sum > 0)
		cout << sum << endl << min;
	else
		cout << "-1";
	return 0;
}