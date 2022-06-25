#include <iostream>
using namespace std;

int reverse(int N)
{
	int a, b, c, d;
	a = N % 10; // 일의 자리
	b = (N / 10) % 10; // 십의 자리
	c = N / 100; // 백의 자리
	d = a * 100 + b * 10 + c;
	return d;
}

int main()
{
	int A, B;
	int C, D;

	cin >> A >> B;
	C = reverse(A);
	D = reverse(B);

	if (C > D)
		cout << C;
	else
		cout << D;
	return 0;
}