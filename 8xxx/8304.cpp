#include <iostream>
#include <map>
using namespace std;

typedef long long lol;

map<pair<lol, lol>, lol> mp;

lol func(lol x, lol y)
{

    lol res = 0;

    if (x <= 0 || y <= 0)
        return 0;

    if (mp.count({x, y}) > 0)
        return mp[{x, y}];

    if (x <= y)
        res = func(x - 1, y - 2) + func(x - 2, y - 1) + 2;
    else if (x > y)
        res = func(x - 2, y - 2) + 1;
    mp[{x, y}] = res;

    return res;
}

int main()
{

    lol x, y;
    cin >> x >> y;
    lol ans = func(x, y);
    cout << ans << endl;

    return 0;

}
