#include <iostream>
#include<cmath>
using namespace std;

int main()
{
	int M, N;
	bool arr[1000001];
	cin >> M >> N;

	for (int i = 2; i < 1000000; i++)
		arr[i] = true;

	arr[1] = false;

	for (int i = 2; i <= sqrt(1000000); i++)
	{
		if (arr[i] == true)
		{
			for (int j = i * i; j < 1000001; j = j + i)
				arr[j] = false;
		}
	}

	for (int i = M; i <= N; i++)
	{
		if (arr[i] == 1)
			cout << i << '\n';
	}
	return 0;

}