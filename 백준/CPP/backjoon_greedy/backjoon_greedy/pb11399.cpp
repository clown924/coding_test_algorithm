#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int N;
	int sum = 0;
	vector <int> V;

	cin >> N; // ����� ��
	for (int i = 0; i < N; i++)
	{
		int x;
		cin >> x;
		V.push_back(x);
	}

	sort(V.begin(), V.end());
	for (int i = 0; i < N; i++)   // if ù ��° = 1, �� ��° = 1 + 2, �� ��° = 1 + 2 + 3, �� ��° = 1 + 2 + 3 + 3 
		sum += V[i] * (N - i); // 1���� 5��, 2���� 4��...
	
	cout << sum;
	return 0;
}