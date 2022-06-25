#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int N; // 사람의 수
	cin >> N;

	vector <pair<int, int>> V;
	vector <int> Count; // 등수

	for (int i = 0; i < N; i++)
	{
		int x , y;
		cin >> x >> y;
		V.push_back(make_pair(x,y));
		Count.push_back(1);
	}

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (V[i].first < V[j].first && V[i].second < V[j].second)
				Count[i]++;
		}
	}
	for (int i = 0; i < N; i++)
		cout << Count[i] << " ";
}