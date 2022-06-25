#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

bool compare(string a, string b)
{
	if (a.length() == b.length())
	{
		for (int i = 0; i < a.length(); i++)
		{
			if (a[i] != b[i])
				return a[i] < b[i];
		}
	}
	return a.length() < b.length();
}

int main()
{
	int N;
	cin >> N;

	vector <string> vec;

	for (int i = 0; i < N; i++)
	{
		string str;
		cin >> str;
		vec.push_back(str);
	}
	sort(vec.begin(), vec.end(), compare);
	cout << vec[0] << "\n";
	for (int i = 1; i < N; i++)
	{
		if (vec[i - 1] == vec[i])
			continue;
		cout << vec[i] << "\n";
	}

}