#include <iostream>
using namespace std;

int main()
{
	int x;
	int result = 0;
	cin >> x;

	int crossNum = 1;
	int Num_in_cross = 0;

	while (x - crossNum > 0)  // x를 입력 받았을 때, 몇 번째 대각선에 있는지 구하기, 그 대각선에서의 x 위치 구하기
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