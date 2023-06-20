#include<bits/stdc++.h>

using namespace std; 


int main()
{ 

    long long t, i, n;

    cin>>n; 

    t = sqrt(n) + 1; 

    for(i = 1; i < t; i++)
    { 
        if(pow(i, 3) < n) 
            cout << pow(i, 3) << " "; 
        else
            break; 
    } 

}
