#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char* argv[])
{
	int t = time(NULL);
	printf("t is %d.\n", t);
	srand(t);
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

	printf("So your choice shall be %s.\n", argv[rand()%argc]);
	printf("bububu.\n");
	return 0;


}
