#include <iostream>
using namespace std;

int main()
{
	int Arr[8];
	int check;
	
	for (int i = 0; i < 8; i++)
	{
		cin >> Arr[i];
	}
	if (Arr[0] == 1)
		check = 1;
	else if (Arr[0] == 8)
		check = -1;
	else
	{
		cout << "mixed";
		return 0;
	}
	if (check == 1)
	{
		for (int j = 0; j < 8; j++)
		{
			if (Arr[j] != j + 1)
			{
				cout << "mixed";
				return 0;
				
			}
		}
		cout << "ascending";
		return 0;
	}
	if (check == -1)
	{
		for (int j = 0; j < 8; j++)
		{
			if (Arr[j] != 8 - j)
			{
				cout << "mixed";
				return 0;
				
			}
		}
		cout << "descending";
		return 0;
	}
}