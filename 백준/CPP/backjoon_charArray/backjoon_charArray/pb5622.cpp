#include <iostream>
using namespace std;

int main()
{
	string str;
	cin >> str;

	int time = 0;
	for (int i = 0; i < str.length(); i++)
	{
		int val = str[i] - 'A'; // 알파벳을 0~26까지로 대입 A = 0;
		if (val < 15)
			time = time + (val / 3) + 3;
		else if (val < 19)
			time += 8;
		else if (val < 22)
			time += 9;
		else
			time += 10;
	}
	cout << time;

	return 0;
}