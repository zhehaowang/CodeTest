#include <stdio.h>

struct s1
{
	int x;
	int *p;
};

int foo(struct s1 s)
{
	s.x = 10;
	return 1;
}

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
	struct s1 s;
	s.x = 1;
	foo(s);
	printf("result is %d\n", s.x);
	return 1;
}
