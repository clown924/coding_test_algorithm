#include <iostream>
using namespace std;

int main()
{
	int n;
	int result = 0;
	int* arr = new int[n];
	for (int i = 0; i < n; i++)
	{
		cin >> arr[i];
		result += arr[i];
	}
	return result;
}