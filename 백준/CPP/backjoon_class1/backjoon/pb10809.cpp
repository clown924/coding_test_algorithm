#include <iostream>
using namespace std;

int main()
{
	string A;
	int B[26];

	cin >> A; // Baekjoon 

	for (int i = 0; i < 26; i++)
	{
		B[i] = -1;
	}

	for (int j = 0; j < A.length(); j++)
	{
		if (B[A[j] - 'a'] == -1)  // A[j] - 'a' �� ������ ����, 'a' ~ 'z' �� 0~26���� �ٲ�.
			B[A[j] - 'a'] = j;
	}

	for (int s = 0; s < 26; s++)
		cout << B[s] << " ";

	return 0;
}