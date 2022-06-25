#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int N;
	int sum = 0;
	vector <int> V;

	cin >> N; // 사람의 수
	for (int i = 0; i < N; i++)
	{
		int x;
		cin >> x;
		V.push_back(x);
	}

	sort(V.begin(), V.end());
	for (int i = 0; i < N; i++)   // if 첫 번째 = 1, 두 번째 = 1 + 2, 세 번째 = 1 + 2 + 3, 네 번째 = 1 + 2 + 3 + 3 
		sum += V[i] * (N - i); // 1분은 5명, 2분은 4명...
	
	cout << sum;
	return 0;
}