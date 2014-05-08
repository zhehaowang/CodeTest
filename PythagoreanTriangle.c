#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int pythaTriangle(int * array, int length, int depth, int * dstArray)
{
	int i = 0;
	int j = 0;
	int k = length;
	int start = 0;
	memcpy(dstArray, array, sizeof(int) * length);
	for (i = 0; i < depth; i++)
	{
		dstArray[k++] = array[0];
		printf("%d\t", dstArray[k - 1]);
		for (j = start; j < start + length + i - 1; j++)
		{
			printf("%d\t", dstArray[j] + dstArray[j+1]);
			dstArray[k++] = dstArray[j] + dstArray[j+1];
		}
		dstArray[k++] = array[length - 1];
		printf("%d\t", dstArray[k - 1]);
		start += (length + i);
		printf("\n");
	}
}

int main()
{
	int dstArray[30] = {0};
	int input[3] = {1, 2, 3};
	pythaTriangle(input, 3, 4, dstArray);
	return 0;
}
