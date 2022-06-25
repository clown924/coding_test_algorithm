#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	double A, B, V;
	double day = 0;
	cin >> A >> B >> V;

	day = (V - B) / (A - B);
	day = ceil(day);
	cout << (int)day;

	return 0;
}