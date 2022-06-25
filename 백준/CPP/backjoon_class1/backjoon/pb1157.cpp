#include <iostream>
#include <string>
using namespace std;

int main()
{
	string A;
	int alpha[26] = { 0 };
	int max = 0, index = 0;
	cin >> A;
	
	for (int i = 0; i < A.length(); i++)
	{
		index = toupper(A[i]);
		alpha[index - 65]++;
	}
	int max_index = 0;
	for (int i = 0; i < 26; i++)
	{
		if (alpha[i] > max)
		{
			max = alpha[i];
			max_index = i;
		}
	}

	int count = 0;
	for (int i = 0; i < 26; i++)
	{
		if (alpha[i] == max)
		{
			count++;
			if (count >= 2)
			{
				cout << "?" << endl;
				return 0;
			}
		}
	}
	cout << (char)(max_index + 65) << endl;
	return 0;
}