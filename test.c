#include <stdio.h>

int main()
{
	printf("hello world.\n");
	int i = 0;
	long sum = 0;
	for (i = 0; i <= 100; i++)
	{
		printf("%ld\t", sum);
		sum += i;
	}
	printf("%ld\n", sum);
	return 1;
}