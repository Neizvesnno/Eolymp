#include<iostream>

using namespace std; 


int main()
{ 

    string a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; 
    string b; 
    int k, i, j; 

    cin >> b >> k; 

    for(int i = 0; i < b.size(); i++) 

        for(int j = 0; j < 26; j++) 

            if(b[i] == a[j])
            { 
                if(j - k >= 0) 

                    cout << a[j-k]; 

                else if(j - k < 0) 

                    cout << a[j + 26 - k]; 

                    break;
            } 

    return 0;

}
