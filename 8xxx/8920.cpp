#include <iostream>

using namespace std; 


int main() 
{ 

    int n; 

    cin >> n; 

    int say = 0,say1 = 1; 

    while(say != n) 
    { 

        if(say1%2 != 0 and say1%3 != 0 and say1%5 != 0) 
        { 
            cout << say1 << " "; 
            say++;
        } 
        say1++; 
    } 

}
