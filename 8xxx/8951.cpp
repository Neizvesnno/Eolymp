#include <iostream>

using namespace std; 


int main() 
{ 

    int n; 
    cin >> n; 
    int k = (n+1)/2; 
    int L = k, R = k; 

    for(int i = 1; i <= k; i++) 
    { 

        for(int j = 1; j <= n; j++) 
        {

            if(j==L or j==R) 
                cout << "*"; 
            else 
                cout << " "; 

        } 

        cout << endl; 
        L--; 
        R++;

    }

    L = 2; 
    R = n - 1; 

    for(int i = 1; i < k; i++)
    { 

        for(int j=1; j<=n; j++)
        { 

            if(j == L or j == R) 
                cout << "*"; 
            else
                cout << " ";

        } 

        cout << endl; 
        L++; 
        R--; 

    } 

}
