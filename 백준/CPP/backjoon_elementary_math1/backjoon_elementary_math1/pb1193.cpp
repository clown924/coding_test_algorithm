#include <iostream>
using namespace std;

int main()
{
	int x;
	int result = 0;
	cin >> x;

	int crossNum = 1;
	int Num_in_cross = 0;

	while (x - crossNum > 0)  // x�� �Է� �޾��� ��, �� ��° �밢���� �ִ��� ���ϱ�, �� �밢�������� x ��ġ ���ϱ�
	{
		x = x - crossNum;
		crossNum++;
	}
	
	if (crossNum % 2 == 0)
		cout << x << "/" << crossNum - x + 1;
	else
		cout << crossNum - x + 1 << "/" << x;

	return 0;
}