#include <iostream>
using namespace std;

int reverse(int N)
{
	int a, b, c, d;
	a = N % 10; // ���� �ڸ�
	b = (N / 10) % 10; // ���� �ڸ�
	c = N / 100; // ���� �ڸ�
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