#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
	/*int N;  // pair 만 사용
	cin >> N;

	pair<int, int> v[100001];

	for (int i = 0; i < N; i++)
		cin >> v[i].second >> v[i].first;
	
	sort(v, v + N);
	for (int i = 0; i < N; i++)
		cout << v[i].second << " " << v[i].first << "\n";*/

	int N;   // vector에 pair를 contain
	cin >> N;

	vector <pair<int, int>> v;
	for (int i = 0; i < N; i++)
	{
		int x, y;
		cin >> x >> y;
		v.push_back(make_pair(y, x));
	}
	sort(v.begin(), v.end());

	for (int i = 0; i < N; i++)
		cout << v[i].second << " " << v[i].first << "\n";
}