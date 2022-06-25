#include <iostream>
using namespace std;

int main()
{
	int A, B, C;
	int Product_num = 1, total_price;
	int B_E_P;
	cin >> A >> B >> C;

	if (B >= C)
	{
		B_E_P = -1;
		cout << B_E_P;
		return 0;
	}
	else
		B_E_P = A / (C - B) + 1;
	cout << B_E_P;

	return 0;

}