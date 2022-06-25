#include <iostream>
using  namespace std;

int main()
{
	int N;
	int i = 2;
	cin >> N;

	for (int i = 2; i <= N; i++)
	{
		while (N % i == 0)
		{
			cout << i << endl;
			N = N / i;
		}
	}
	if (N != 1)
		cout << N;

	return 0;
}