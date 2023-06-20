#include<iostream>

using namespace std; 


int main() 
{

    long long p, q, n, t = 0;

    cin>>n; 

    long long a[n][n]; 

    p = n / 2; 
    q = p; 

    bool r = true; 

    for(long long i = 0; i < n; i++)
    { 

        for(long long j = 0; j < n; j++)
        { 

            if(j >= p && j <= q)
            { 

                cout<<"*"; 

            } 
            else
            { 

                cout<<" "; 

            } 
        } 

        if(p == 0)
        { 

            r = false; 

        } 

        if(r == true)
        { 

            q++;
            p--; 

        } 
        else
        { 

            q--;
            p++; 

        } 

        cout<<endl; 

        } 

}
