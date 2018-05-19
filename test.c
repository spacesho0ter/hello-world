#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

int main(int argc, char* argv[])
{
	int t = time(NULL);
	int length;
	char* tgt; 
	printf("t is %d.\n", t);
	srand(t);
	if(argc <= 0)
	{
		printf("hehe.\n");
		return 0;
	}	
	int i = 1;
	while(i<argc)
	{
		printf("imput %d is: %s.\n", i, argv[i]);
		i++;
	}
	tgt = argv[rand()%argc+1];
	length = strlen(tgt);
	printf("So your choice shall be %s,", tgt);
	printf("length is:%d,  ", length);
	printf("Each word is:\n");
	for(i = 0;i<length;i++)
	{
		printf("%d,%c|", tgt[i],tgt[i]);
	}
	printf("\n");
	printf("bububu.\n");
	return 0;


}
