#include<unistd.h>
#include<stdio.h>
#include<fcntl.h>
#include<stdlib.h>
int main()
{
	FILE *f;
	f = fopen("process_tree.txt","w");
		int pid,p,i,n,ab;
    	p=getpid();                
    	printf("enter the number of levels\n");fflush(stdout);
    	scanf("%d",&n); 
    	fflush(stdout);               
    	printf("root %d\n",p);

    for(i=0;i<n;i++)
    {	
        pid=fork();
        if(i >0){
      fprintf(f,"%d %d ",getppid(),getpid());fflush(stdout);
        waitpid(pid,&ab,0);
        }                     
        
    }   
    fprintf(f,"%d %d ",getppid(),getpid());fflush(stdout);
        waitpid(pid,&ab,0);
    return 0;

fclose(f);
}
