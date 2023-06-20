#include<iostream>

typedef long long lol;

using namespace std; 

int main() 
{ 

    string s; 
    getline(cin,s); 
    lol gt, say = 1, t = 0; 

    for(int i = 0; i < s.size(); i++) 
    { 

        if(s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U' || s[i] == 'Y') 
        {
 
            if(say > t) 
                t = say; 

            say = 1; 
        } 
        else 
            say++; 

        if(say > t)
            t = say; 

    }

    cout << t;
 
    return 0; 

}
