#include <bits/stdc++.h>
using namespace std; 


int gcd(int a, int b)
{ 
    return b == 0 ? a : gcd(b, a%b); 
} 


int main() 
{ 
    int n, t; cin>>t; while(t--)
    { 
        cin>>n; 
        int a[n]; 
        for(int i = 0; i < n; i++)
        { 
            cin>>a[i]; 
        } 
        int g = 0; 
        for(int i = 0; i < n-1; i++)
        { 
            for(int j = i+1; j < n; j++)
            { 
                g += gcd(a[i], a[j]); 
            } 
        } 
        cout<<g<<endl; 
    } 
}
