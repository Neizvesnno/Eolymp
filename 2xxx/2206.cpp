#include <iostream>
#include<string>

using namespace std;


int main() 
{ 
    long a,b,c; 
    cin>>a>>b>>c; 
    long h=(a+b+c)/3; 
    unsigned k=0; 
    if((a+b+c)%3==0) 
    { 
        k=k+abs(h-a); 
        k=k+abs(h-b); 
        k=k+abs(h-c); 
        cout<<k/2; 
    } 
    if((a+b+c)%3!=0) 
        cout<<"IMPOSSIBLE"; 
}
