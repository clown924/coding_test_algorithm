#include <iostream>
using namespace std;

int main()
{
	int x, y, w, h;
	int result[2];

	cin >> x >> y >> w >> h;

	if (abs(x - w) > abs(y - h))
		result[0] = abs(y - h);
	else
		result[0] = abs(x - w);

	result[1] = x > y ? y : x;

	if (result[0] < result[1])
		cout << result[0];
	else
		cout << result[1];

	return 0;
}