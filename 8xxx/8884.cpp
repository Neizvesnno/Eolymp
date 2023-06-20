#include<iostream>

using namespace std; 


int main() 
{ 

    long long a,b,c; 
    cin >> a >> b >> c; 

    if((a == b && b == c && c == a) and (a < b + c and b < a + c and c < b + a))
    { 
        cout << "equilateral"; 
    } 
    else if((a == b && a + b > c) || (a == c && a + c > b ) || (b == c && b + c > a) and (a < b + c and b < a + c and c < b + a))
    { 
        cout << "isosceles"; 
    } 
    else if(a != b && b != c && c != a and (a < b + c and b < a + c and c < b + a))
    {
        cout << "versatile"; 
    } 
    else if((a >= b + c or b >= a + c or c >= b + a))
    { 
        cout << "invalid";
    }

}
      
