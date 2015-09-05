#include <stdio.h>
#include <stdlib.h>

int printStar(int n)
{
	if (n > 1)
	{
		printStar(n - 1);
	}
	int i = 0;
	for (i = 0; i < n; i++)
	{
		printf("*");
	}
	printf("\n");
}

int printStarOpposite(int n)
{
	int i = 0;
	for (i = 0; i < n; i++)
	{
		printf("*");
	}
	printf("\n");
	if (n > 1)
	{
		printStarOpposite(n - 1);
	}
}

int main()
{
	int i = 5;
	printStar(i);
	printf("\n");
	printStarOpposite(i);
}