#include <iostream>
using namespace std;

int main()
{
	int testCase;
	cin >> testCase;

	int floor;
	int ho;
	int stair[15][15] = { 0, };  // [��][ȣ]

	for (int i = 0; i < 15; i++)  // 0��
		stair[0][i] = i;

	for (int j = 1; j < 15; j++) // 1ȣ
		stair[j][1] = 1;


	for (int j = 1; j < 15; j++)  // 1��
	{
		for (int h = 1; h < 15; h++)  // 3ȣ
		{
			stair[j][h] = stair[j - 1][h] + stair[j][h - 1];
		}
	}

	for (int i = 0; i < testCase; i++)
	{
		cin >> floor;
		cin >> ho;
		cout << stair[floor][ho] << endl;
	}

	return 0;
}