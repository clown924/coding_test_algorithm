#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

bool compare(pair<int,string>a,pair<int,string>b)
{
	return a.first < b.first;
}

int main()
{
	int N;
	cin >> N;

	vector<pair<int, string>> vec;
	for (int i = 0; i < N; i++)
	{
		int x;
		string str;

		cin >> x >> str;
		vec.push_back(make_pair(x,str));
	}
	stable_sort(vec.begin(), vec.end(),compare);

	for (int i = 0; i < N; i++)
	{
		cout << vec[i].first <<" "<< vec[i].second << "\n";
	}
}