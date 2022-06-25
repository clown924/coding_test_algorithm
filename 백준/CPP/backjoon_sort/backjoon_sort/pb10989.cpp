#include <iostream>
using namespace std;

int main() // 카운트 정렬( 계수 정렬 )
{
	ios_base::sync_with_stdio(false); 
	cin.tie(NULL); 
	cout.tie(NULL);

	int N,tmp;
	cin >> N;

	int count[10001] = { 0, };

	for (int j = 0; j < N; j++)
	{
		cin >> tmp;
		count[tmp]++;
	}
	
	for (int i = 1; i < 10001; i++)
		for (int j = 0; j < count[i]; j++)
			cout << i << "\n";

	return 0;

}