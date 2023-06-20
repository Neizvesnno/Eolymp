#include<iostream>
#include<cmath>

using namespace std; 

int main() 
{ 
    int i; 
    bool e = true; 

    cin >> i; 

    if(i == 2) 
        cout << 2; 
    else 
    {
        for(int u = 3; u <= sqrt(i); u++) 
            if(i%u == 0) 
            { 
                e = false; 
                cout << u; 
                return 0; 
            } 

            if(e == true) 
                cout<<i; 
                return 0; 
    } 
}
