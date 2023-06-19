#include <iostream>
#include <string>

using namespace std;


int strl(const char* a, char b)
{
	int count = 0, cinso = 0;

	for (count = 0; a[count] != '\0'; count++)
	{
		if (a[count] == b)
		{
			cinso++;
		}
	}

	return cinso;

}


int main()
{

	char a[100] = "";
	char b;

	cin >> a;
	cin >> b;

	cout << strl(a, b) << endl;

}
