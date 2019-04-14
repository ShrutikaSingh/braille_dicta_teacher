#include<stdio.h>
#include<math.h>

char str[33]={'\0'};

void dec_bin(int);
void bin_dec(long int);

void main()
{
 int num;
 printf("Enter num:");
 scanf("%d",&num);
 dec_bin(num);
 
}

void dec_bin(int num)

{
 int i,j=0,bit=0; 
 long int data;
 for(bit=31;bit>=0;bit--)
  { 
   if((num>>bit)&1)
   { 
     str[j]='1';
     j++; 
   }
   else
   {
    str[j]='0';
    j++;
   }
  } 
 printf("%s\n",str);
 data=atoi(str);
 //bin_dec(data);
 printf("data tobe send:%ld\n",data); 
 bin_dec(data);

}

void bin_dec(long int n)
{
  int rem,i=0;
  long int data=0;
  while(n!=0)
  {
    rem=n%10;
    n/=10;
    data=data+(rem*pow(2,i)); 
    i++;
  }
  printf("new data :%ld\n",data);  
  
}  

