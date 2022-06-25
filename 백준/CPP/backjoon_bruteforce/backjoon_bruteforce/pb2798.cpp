#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int N, M; // N -> 카드의 개수, M -> 만들어야 하는 숫자
	cin >> N >> M;
	vector <int> card;
	int sum = 0;
	int result = 0;

	for (int i = 0; i < N; i++)
	{
		int x;
		cin >> x;
		card.push_back(x);
	}

	for (int i = 0; i < N - 2; i++)
	{
		for (int j = i + 1; j < N - 1; j++)
		{
			for (int k = j + 1; k < N; k++)
			{
				sum = card[i] + card[j] + card[k];
				if (sum > result && sum <= M)
					result = sum;
			}
		}
	}

	cout << result;

}