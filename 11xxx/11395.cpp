#include <iostream>

using namespace std;


int main() 
{ 
    int n; 

    cin >>n; 

    int L = 1, R = n; 

    for(int i = 1; i <= n; i++) 
    { 
        for(int j = 1; j <= n; j++) 
        { 
            if(i == j) 
                cout << '@'; 
            if(i < j) 
                cout << '\\'; 
            if(j < i) 
                cout <<'/'; 
        } 

        cout <<'\n'; 
        L++; 
        R--; 

    } 

}
