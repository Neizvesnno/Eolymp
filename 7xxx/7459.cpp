#include <bits/stdc++.h>

#define ll long long

using namespace std; 


int main() 
{ 

    ll n, a, b, c, d, e; 

    cin >> n; 

    a = n / 10000; 
    b = n / 1000 % 10; 
    c = n / 100 % 10; 
    d = n / 10 % 10; 
    e = n % 10; 

    cout << abs(a * c * e); 

}
