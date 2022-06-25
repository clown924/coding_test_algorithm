#include <iostream>
using namespace std;

int d[1001];

int dp(int N)
{
	if (N == 1)
		return 1;
	if (N == 2)
		return 2;
	if (d[N] != 0)
		return d[N];
	return d[N] = (dp(N - 1) + dp(N - 2)) % 10007;

}

int main()
{
	int N;
	cin >> N;

	cout << dp(N);
}

