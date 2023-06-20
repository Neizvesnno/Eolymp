#include <bits/stdc++.h>
using namespace std;

void solve()
{

    int n;
    cin >> n;
    map<int, int> mp;
    int mx = 0;
    vector<int> v(n);

    for(int i = 0; i < n; i++)
    {
        cin >> v[i];
        mp[v[i]]++;
        if(mp[v[i]] > mx)
            mx = mp[v[i]];
    }

    stack<int> st;
    for(int i = n - 1; i >= 0; i--)
        if(mp[v[i]] == mx)
            mp[v[i]] = 0, st.push(v[i]);


    cout << mx << endl;

    while(!st.empty())
    {
        cout << st.top() << " ";
        st.pop();
    }

}

int main()
{

    solve();

}
