#include<bits/stdc++.h>

using namespace std;


int main() 
{ 
    long a; 

    cin >> a; 

    long b; 

    cin >> b; 

    long cem = 0; 

    if(a > b) 
        swap(a,b); 

    for(int i = a; i <= b; i++) 
    { 
        if(i%2 != 0) 
            cem += i; 
    } 

    cout << cem; 

}
