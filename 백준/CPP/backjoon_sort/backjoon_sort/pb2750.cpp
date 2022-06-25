#include <iostream>
using namespace std;

int main()
{
	int N;
	cin >> N;

	int* arr = new int[N];

	for (int i = 0; i < N; i++)
		cin >> arr[i];
	
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N - 1; j++)
		{
			if (arr[j] >= arr[j + 1])
			{
				int temp;

				temp = arr[j + 1];
				arr[j + 1] = arr[j];
				arr[j] = temp;
			}
		}
	}

	for (int s = 0; s < N; s++)
		cout << arr[s] << endl;
}