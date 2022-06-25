#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int N, K;
	int result = 0;
	cin >> N >> K;

	vector <int> V;
	for (int i = 0; i < N; i++)
	{
		int x;
		cin >> x;
		V.push_back(x);
	}
	for (int i = V.size() - 1; i >= 0; i--)
	{
		result += K / V[i];
		K %= V[i];
	}
	cout << result;
	return 0;
}