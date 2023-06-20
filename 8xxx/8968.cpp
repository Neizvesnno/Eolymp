#include <bits/stdc++.h>
using namespace std;

void solve()
{
    int n;
    cin >> n;
    int arr[n];
    int a, b;

    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];

        if (!i)
            a = arr[0], b = arr[0];
        else
            a = max(a, arr[i]), b = min(b, arr[i]);
    }

    a /= 2, b /= 2;

    for (int i = 0; i < n; i++)
    {
        if (arr[i] > 0)
            arr[i] -= a;
        else if (arr[i] < 0)
            arr[i] -= b;

        cout << arr[i] << " ";
    }

    cout << endl;

}

int main()
{

    solve();

}
