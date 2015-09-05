#include <stdio.h>
#include <stdlib.h>

int reverseBits(int *array, int a, int b)
{
	if ( a < 0 || b < 0 || a > 30 || b > 30)
	{
		printf("Negative input\n");
		return 0;
	}
	if (((*array >> a) & 1) != ((*array >> b) & 1))
	{
		int rev = (1<<a) + (1<<b);
		*array = (*array) ^ rev;
	}
	return 1;
}

int main()
{
	int input = 23;
	reverseBits(&input, 2, 3);
	printf("%d\n", input);
	return 0;
}