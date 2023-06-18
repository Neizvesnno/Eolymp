#include <iostream>
using namespace std;

typedef long long ll;
typedef long double ld;

void solve()
{

    ll s, sum = 1, d = 1, ans = 1;

    cin >> s;

    while (sum < s)
    {
        ans++;
        d = d * 2 + ans;
        sum += d;
    }

    cout << ans << endl;

}


int main()
{

    solve();
    return 0;

}
