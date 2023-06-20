#include <bits/stdc++.h>
using namespace std;

void solve()
{

    int n;
    cin >> n;
    int ans = 0;
    vector<int> v(n);
    map<int, int> mp;

    for (int i = 0; i < n; i++)
    {
        cin >> v[i];
        mp[v[i]]++;
        if (mp[v[i]] > ans)
            ans = mp[v[i]];
    }

    cout << ans << endl;
    set<int> st;

    for (int i = 0; i < n; i++)
        if (mp[v[i]] == ans && st.count(v[i]) == 0)
        {
            cout << v[i] << " ";
            st.insert(v[i]);
        }

}

int main()
{

    solve();

}
