#include <iostream>
using namespace std;

bool hansoo(int num);

int main()
{
	int N;
	int count = 0;
	bool check = false;
	cin >> N;

	for (int i = 1; i <= N; i++)
	{
		check = hansoo(i);
		if (check == true)
			count++;
		else
			continue;
	}
	cout << count;
}

bool hansoo(int num)
{
	int dif[3];

	if (num < 100)
		return true;
	else
	{
		dif[0] = num / 100;
		dif[1] = (num % 100) / 10;
		dif[2] = (num % 100) % 10;
		if ((dif[0] - dif[1]) == (dif[1] - dif[2]))
			return true;
		else
			return false;
	}
}