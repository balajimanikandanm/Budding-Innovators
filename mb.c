#include<stdio.h>
#include<conio.h>
void main()
{
  int a;
printf("enter the number:\n");
scanf("%d",&a);
if(a>0)
{
  printf("the number is positive \n");
}
else if(a<0)
{ 
  printf("the number is negative \n");
}
else
{
  printf("it is zero \n");
}
  getch();
}
