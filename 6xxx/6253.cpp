#include<iostream>
#include<string>

using namespace std;

int solve(string& b, string& a)
{

    if (a == b)
    {
        cout << 0 << endl;
        return 0;
    }

    int len_b = b.length(), len_a = a.length();
    int replic = 0, zap_b = len_b, zap_a = len_a;

    while (b[replic] && b[replic] == a[replic])
    {
        replic++;
    }

    while (zap_b >= 0 && zap_a >= 0 && b[zap_b] == a[zap_a])
    {
        zap_b--;
        zap_a--;
    }

    cout << max(max(0, len_a - len_b), zap_a - replic + 1) << endl;

    return 0;

}

int main()
{

    string b, a;
    cin >> b >> a;

    solve(b, a);

}
