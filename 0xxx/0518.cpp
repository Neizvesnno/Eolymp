#include <iostream>
#include <string>

using namespace std;


int main()
{

	int pb = 0;
	int t, zap; 
	int a, b;
	int arr[101];

	cin >> t;
	zap = t;

	while (t > 0)
	{

		cin >> a;
		cin >> b;

		arr[pb] = a + b;

		pb++;
		t--;

	}

	for (int i = 0; i != zap; i++)
	{

		cout << arr[i] << endl;

	}

}
