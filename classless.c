#include<stdlib.h>
#include<stdio.h>
#include<math.h>

int main()
{
    int net_id[3], nod, count;
    
    printf("Enter the network id:- ");
    scanf("%d.%d.%d",&net_id[0],&net_id[1],&net_id[2]);
    
    printf("Please enter the number of departments: ");
    scanf("%d",&nod);
    
    int dept[nod], number[nod], i, flag=0;
    printf("\n");
    
    for(i=0;i<nod;i++)
    {
        printf("Enter the number of hosts in dept %d: ", i+1);
        scanf("%d", &dept[i]);
    }
    printf("\n");
    
    for(i=0;i<nod;i++)
    {
        int x=0;
        while(dept[i] > pow(2,x))
        	x++;
        number[i]= 32-x;
        if(number[i]==count)
        	net_id[2]+=1;
        printf("The subnet id of Dept %d is: %d.%d.%d/%d \n", i+1, net_id[0], net_id[1], net_id[2], number[i]);
        count=number[i];
    }

    for(i=0;i<nod;i++)
    {
        if(number[i]==number[i+1])
        	flag=flag+1;
    }

    if(flag==nod-1)
    {
        int add=check(net_id[2]);
        printf("\n%d\n",add);
        printf("\nThe summarized subnet id of all Depts is: %d.%d/%d \n", net_id[0], net_id[1], 16+add);
    }
    
    else
    	printf("\nSummarized subnet id for the departments provided is not possible.\n");
}

int check(int count)
{
	int val;
	if(count==1) 
		val=7;
    else if(count==2 || count==3)
		val=6;
    else if(count==4) 
		val=5;
    else if(count<=8 && count>4)
		val=4;
    else if(count<=16 && count>8)
		val=3;
    else if(count<=32 && count>16) 
		val=2;
    else if(count<=64 && count>32) 
		val=1;
    else 
		val=0;
     return val;
}

