#include <stdio.h>
#include <math.h>
 
double f(double x,double y)  
{  

    return x*x +sin(x*y)-y*y;  

}


int main()  
{  
    double x,y;  

    while(scanf("%lf %lf",&x,&y)==2)  
    {  

        f(x,y);  
        printf("%.4lf\n",f(x,y)); 
 
    }
  
    return 0;  
}
