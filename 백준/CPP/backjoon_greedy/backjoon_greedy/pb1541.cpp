#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
	string str;
	int result = 0;
	string temp = "";
	bool minus = false;

	cin >> str;

	for (int i = 0; i <= str.size(); i++)
	{
		if (str[i] == '+' || str[i] == '-' || str[i] == '\0')
		{
			if (minus)
				result -= stoi(temp);
			else
				result += stoi(temp);
			temp = "";
			if (str[i] == '-')
				minus = true;

			continue;
		}
		temp += str[i];
	}
	cout << result;
}