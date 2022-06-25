#include <iostream>
using namespace std;

void palindrome(string A);

int main()
{
	string A;
	
	while (1)
	{
		cin >> A;
		if (A[0] == '0')
			break;
		else
		{
			palindrome(A);
			continue;
		}
	}
	return 0;
}

void palindrome(string A)
{
	int check = 1;
	for (int i = 0; i < A.length()/2; i++)
	{
		if (A[i] != A[A.length() - i - 1])
		{
			check = 0;
			break;
		}
	}
	if (check)
		cout << "yes" << endl;
	else
		cout << "no" << endl;
}