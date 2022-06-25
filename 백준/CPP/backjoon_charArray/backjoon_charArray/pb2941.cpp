#include <iostream>
using namespace std;

int main()
{
	string str;
	cin >> str;
	int count = 0;

	for (int i = 0; i < str.length(); i++)
	{
		if ((str[i] >= 'a' && str[i] <= 'z') || str[i] == '=' || str[i] == '-')
		{
			count++;
			if (str[i] == 'c' && str[i + 1] == '=')
			{
				count--;
				continue;
			}
			else if (str[i] == 'c' && str[i + 1] == '-')
			{
				count--;
				continue;
			}
			else if (str[i] == 'd' && str[i + 1] == 'z')
			{
				if (str[i + 2] == '=')
				{
					count--;
					continue;
				}
			}
			else if (str[i] == 'd' && str[i + 1] == '-')
			{
				count--;
				continue;
			}
			else if (str[i] == 'l' && str[i + 1] == 'j')
			{
				count--;
				continue;
			}
			else if (str[i] == 'n' && str[i + 1] == 'j')
			{
				count--;
				continue;
			}
			else if (str[i] == 's' && str[i + 1] == '=')
			{
				count--;
				continue;
			}
			else if (str[i] == 'z' && str[i + 1] == '=')
			{
				count--;
				continue;
			}
			continue;
		}
	}
	cout << count;

	return 0;
}