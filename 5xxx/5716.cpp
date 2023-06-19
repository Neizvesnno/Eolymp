#include<iostream>
#include<cmath>

using namespace std; 


int main()
{ 
    long long n, r = 0; 
    cin>>n; 
    for(int i=1;i<=n;i++)
    { 
        r=r+i*2+i-1;
    }

    cout<<r;

}
