#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	int N;
	int ans = 0;
	int cnt = 0;
	int title = 665;
	string str;
	cin >> N;

	while (title++)
	{
		str = to_string(title);
		if (str.find("666") != -1)
			N--;
		
		if (N == 0)
		{
			cout << title << endl;
			break;
		}
	}
}