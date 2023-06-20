#include <bits/stdc++.h>

using namespace std; 


float s(float x) 
{ 

    return x + sin(x); 

} 


int main() 
{ 

    float x; 
    cin >> x; 
    cout << setprecision(4) << fixed; 
    cout << s(x); 

}
