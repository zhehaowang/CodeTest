#include <stdio.h>
#include <stdlib.h>

void hanoi(int plate, int source, int dest, int spare)
{
	if (plate == 1)
	{
		printf("%d : %d -> %d\n", plate, source, dest);
	}
	else
	{
		hanoi(plate - 1, source, spare, dest);
		printf("%d : %d -> %d\n", plate, source, dest);
		//used to be wrong logic;
		hanoi(plate - 1, spare, dest, source);
	}
}

int main()
{
	hanoi(3, 1, 2, 3);
	return 0;
}