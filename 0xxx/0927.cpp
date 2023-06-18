#include <iostream>

using namespace std; 


int main() 
{ 

    int n;
    int qiymet = 0; 
    double a, b;

    cin>>n; 

    for(int i=0;i<n;i++) 
    { 

        cin>>a>>b; 

        if(b<50) 
            qiymet += a;

    } 

    cout<<qiymet; 

}
