#include <iostream>
#include <string>
using namespace std;

int main()
{
	string A;
	getline(cin, A);

	int count = 0;

	if (A.empty())
	{
		cout << "0";
		return 0;
	}
	count = 1;
	for (int i = 0; i < A.length(); i++)
	{
		if (A[i] == ' ')
			count++;
	}
	if (A[0] == ' ')
		count--;
	if (A[A.length() - 1] == ' ')
		count--;
	cout << count;
	return 0;
}
