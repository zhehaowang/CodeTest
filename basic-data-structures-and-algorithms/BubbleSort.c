#include <stdio.h>
#include <stdlib.h>

#define SIZE 5

int bubbleSort(int * array, int length)
{
	int i = 0, temp = 0, j = 0;
	for (i = length - 1; i > 0; i--)
	{
		for (j = 0; j < i; j++)
		{
			if (array[j] > array [j+1])
			{
				temp = array[j];
				array[j] = array [j+1];
				array[j+1] = temp;
			}
		}
	}
	return 1;
}

int printArray(int * array, int length)
{
	int i = 0;
	for (i = 0; i < length; i++)
	{
		printf("%d\t", array[i]);
	}
	printf("\n");
}

int main()
{
	int array[SIZE] = {5, 4, 3, 2, 1};
	bubbleSort(array, SIZE);
	printArray(array, SIZE);
	return 0;
}