#include<bits/stdc++.h>

using namespace std; 

int main()
{ 

    string s;
    getline (cin,s); 

    for(int i = 0; i < s.size(); i++)
    { 
        if(i == 0)
            cout << s[i];
        else if(s[i] == s[i-1])
            continue; 
        else 
            cout<<s[i]; 
    }

}
