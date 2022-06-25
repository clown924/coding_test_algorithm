#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int mode(int* arr, int N);

int main()
{
	int N;
	double avreage = 0;
	int mid_value;

	cin >> N;
	if (N % 2 == 0)
		return 0;
	
	int* arr = new int[N + 1];

	for (int i = 1; i <= N; i++)
		cin >> arr[i];

	for (int i = 1; i <= N; i++)
		avreage += arr[i];
	avreage = avreage / N;
	cout << round(avreage) << "\n";

	sort(arr + 1, arr + N + 1);
	mid_value = (N + 1) / 2;
	cout << arr[mid_value] << "\n";

	int compare[8001] = { 0 };

	for (int i = 1; i <= N; i++)
		compare[arr[i] + 4000]++;

	int cnt = 0;
	for (int i = 0; i < 8001; i++)
	{
		if (cnt < compare[i])
			cnt = compare[i];
	}

	int try1 = 1;
	int mode;

	for (int i = 0; i < 8001; i++)
	{
		if (cnt == compare[i])
		{
			if (try1 == 2)
			{
				mode = i;
				break;
			}
			try1++;
			mode = i;
		}
	}

	cout << mode - 4000 << "\n";
	cout << arr[N] - arr[1] << "\n";

}