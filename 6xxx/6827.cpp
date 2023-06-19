#include<iostream>
#include<string>

using namespace std;

int main()
{

    string s, x;

    cin >> s;

    cin >> x;

    if(x.size() <= s.size())
        cout << "go" << endl;
    else
        cout << "no" << endl;

    return 0;

}
