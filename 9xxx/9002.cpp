#include <bits/stdc++.h>

using namespace std; 


int main()
{ 

    long long cem = 0; 
    long long a, b, n; 

    cin >> n >> a >> b; 

    cem = n/2*a + n/2*b; 

    if(n%2 == 1)
    { 

        cem += max(a, b); 

    } 

    cout << cem << endl; 

}
