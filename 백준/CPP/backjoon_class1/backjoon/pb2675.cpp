#include <iostream>
#include <string>
using namespace std;

string solution(int repeat, string str)
{
	string result = "";
	for (int i = 0; i < str.length(); i++)
	{
		for (int j = 0; j < repeat; j++)
		{
			result += str[i];
		}
	}
	return result;
}

int main()
{
	int testCase;

	cin >> testCase;
	for (int i = 0; i < testCase; i++)
	{
		int repeat;
		cin >> repeat;

		string str;
		cin >> str;
		cout << solution(repeat, str) << endl;
	}

	return 0;
}

