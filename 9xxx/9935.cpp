#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;

void solve()
{

    int n;
    cin >> n;
    int d = n / (60 * 24);
    int ost = n - d * 60 * 24;
    int h = ost / 60;
    int m = ost - h * 60;

    cout << d + 1 << " " << h << " " << m << endl;
}

int main()
{

    solve();

    return 0;
  
}
