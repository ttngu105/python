#include<unistd.h>
#include<stdio.h>
#include<fcntl.h>
#include<stdlib.h>
int main()
{
	FILE *f, *lvl;
	f = fopen("process_tree.txt","w");
    lvl = fopen("lvl.txt","w");
		int pid,p,i,n,ab;
    	p=getpid();                
    	printf("enter the number of levels\n");fflush(stdout);
    	scanf("%d",&n); 
    	fflush(stdout);               
    	printf("root %d\n",p);

    for(i=0;i<n;i++)
    {	
        pid=fork(); 
        fflush(stdout);
        fprintf(f,"%d %d %d",getpid(),getppid(),i); 
    }   
        waitpid(pid,&ab,0);
    return 0;

fclose(f);
}
