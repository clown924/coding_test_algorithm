#include <iostream>
using namespace std;

int main()
{
	int n;
	int check = 0;
	for (int i = 0; i < 5; i++)
	{
		cin >> n;
		check += (n * n);
	}
	check = check % 10;
	cout << check << "\n";
	return 0;
}