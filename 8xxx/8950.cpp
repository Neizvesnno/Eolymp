#include<stdio.h>

using namespace std;


int main()
{ 

    int n, i, j;

    scanf("%d",&n); 

    for(i = 1; i <= n; i++)
    { 

        for(j = 1; j <= n; j++)
        { 
            if(j == n - i + 1 or j == i or (i > j and i + j <= n) or (j > i and i + j > n)) 
                printf("*"); 
            else 
                printf(" "); 
        } 

        printf("\n"); 

    } 

}
