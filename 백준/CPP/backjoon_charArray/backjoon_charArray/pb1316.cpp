#include <iostream>
using namespace std;

int main()
{
	int testCase;
	int cnt = 0;
	cin >> testCase;

	for (int i = 0; i < testCase; i++)
	{
		string str;
		cin >> str;

		cnt++;

		bool arr[26] = { false, };
		for (int j = 0; j < str.length(); j++)
		{
			char ch = str[j] - 'a';
			if (arr[ch] == false)
				arr[ch] = true;
			else
			{
				if (str[j] != str[j - 1])
				{
					cnt--;
					break;
				}
			}
		}

	}
	cout << cnt;
	return 0;
	
}