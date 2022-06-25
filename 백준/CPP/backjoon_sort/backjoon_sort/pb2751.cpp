#include <iostream>
#include <algorithm>

using namespace std;

int main() // sort 함수( algorithm 헤더 )
{
	int N;
	cin >> N;

	int* arr = new int[N];
	
	for (int i = 0; i < N; i++)
	{
		cin >> arr[i];
	}
	sort(arr, arr + N);

	for (int j = 0; j < N; j++)
		printf("%d\n", arr[j]);

	return 0;
}