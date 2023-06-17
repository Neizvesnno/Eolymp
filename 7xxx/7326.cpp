#include <bits/stdc++.h>

using namespace std;


int main() 
{ 
    string s;

    cin >> s; 

    int k = 0; 
    int p = 0; 

    for (char c : s) 
    { 

        if (c == 'k') 
        { 
            p++; 
        } 
        else 
        { 
            k = max(k, p); 
            p = 0; 
        } 

    } 

    k = max(k, p); 
    cout << k << endl;
}
