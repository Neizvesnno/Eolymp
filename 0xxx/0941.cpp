#include<stdio.h>
#include<stdlib.h>

int main()
{ 
  
  int a,b,c,d,s,x,r;
  
  scanf("%d",&a);
  b=abs(a/100);
  c=abs(a%100/10);
  d=abs(a%10);
  s=b+c+d;
  x=b*c*d;
  r=x-s;
  
  printf("%d\n",r);
  
  return 0;
  
}
