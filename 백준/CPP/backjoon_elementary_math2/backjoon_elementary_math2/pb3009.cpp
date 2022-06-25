#include <iostream>
using namespace std;

int main()
{
	int arr[6];
	int x, y;

	cin >> arr[0] >> arr[1];
	cin >> arr[2] >> arr[3];
	cin >> arr[4] >> arr[5];

	if (arr[0] != arr[2])
	{
		if (arr[0] == arr[4])
			x = arr[2];
		else
			x = arr[0];
	}
	if (arr[0] == arr[2])
		x = arr[4];

	if (arr[1] != arr[3])
	{
		if (arr[1] == arr[5])
			y = arr[3];
		else
			y = arr[1];
	}
	if (arr[1] == arr[3])
		y = arr[5];

	cout << x << ' '<<y;
}