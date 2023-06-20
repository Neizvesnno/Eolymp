#include<bits/stdc++.h>

using namespace std; 


int main() 
{ 

    int a,b,c; 

    cin>>a>>b>>c; 

    if(a==b && a+b>c || a==c && a+c>b || b==c && b+c>a) 
    {

        cout<<a+b+c; 

    }
    else 
    {

        cout<<"No"; 

    }

}
