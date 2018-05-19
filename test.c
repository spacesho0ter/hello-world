#include <stdio.h>

int main(int argc, char* argv[])
{
	if(argc <= 0)
	{
		printf("hehe.\n");
		return 0;
	}	
	int i = 0;
	while(i<argc)
	{
		printf("imput %d is: %s.\n", i, argv[i]);
		i++;
	}
	printf("bububu.\n");
	return 0;


}
