#include <iostream>
using namespace std;

int d[1001];

int dp(int N)
{
	if (N == 0)
		return 1;
	if (N == 1)
		return 0;
	if (N == 2)
		return 3;
	if (d[N] != 0)
		return d[N];
	int result = 3 * dp(N - 2);
	for (int i = 3; i <= N; i++)
	{
		if (i % 2 == 0)
			result += 2 * dp(N - i);
	}
	return d[N] = result;
}

int main()
{
	int N;
	cin >> N;

	cout << dp(N);
}