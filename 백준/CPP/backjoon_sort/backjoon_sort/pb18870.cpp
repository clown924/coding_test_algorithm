#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
	int N;
	cin >> N;

	vector<int> vec, count;
	
	for (int i = 0; i < N; i++) // 입력받음
	{
		int x;
		cin >> x;
		vec.push_back(x);
		count.push_back(x);
	}
	
	sort(count.begin(), count.end());

	count.erase(unique(count.begin(), count.end()), count.end());

	for (int i = 0; i < N; i++)
		cout << lower_bound(count.begin(), count.end(), vec[i]) - count.begin() << "\n";
}