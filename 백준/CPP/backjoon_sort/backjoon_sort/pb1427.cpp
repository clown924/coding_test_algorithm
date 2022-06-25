#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	string str;
	cin >> str;

	sort(str.begin(), str.end(),greater<char>()); // default >> 오름차순,    greater<char>() >> 내림차순,
	cout<<str;

	return 0;
}