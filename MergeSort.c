//Started May 1st, 10:10PM, medium status, just read merge sort before implementation
//Untested on May 1st by night

#include <stdio.h>
#include <stdlib.h>

#define LENGTH 5

int mergeSort(int *array, int begin, int end, int * dstArray)
{
	int mid = (end - begin) >> 1;
	if (!mid)
	{
		return 0;
	}
	mergeSort(array, begin, mid, dstArray);
	mergeSort(array, mid, end, dstArray);
	merge(array + begin, array + mid, dstArray + begin, mid - begin, end - mid);
	memcpy(array + begin, dstArray + begin, end - begin);
return 0;
}

int printArray(int * array, int length)
{
	int i = 0;
	for (i = 0; i < length; i++)
	{
		printf("%d\t", array[i]);
	}
	printf("\n");
	return 0;
}

int merge(int * src1, int * src2, int * dst, int length1, int length2)
{
	int i = 0;
	int j = 0;
	int k = 0;
	while ( i < length1 && j < length2)
	{
		if (src1[i] > src2[j])
		{
			dst[k++] = src1[i++];
		}
	}
	return 0;
}

int main()
{
	int array[LENGTH] = {1, 2, 3, 4, 5};
	int dstArray[LENGTH] = {0};
	printArray(array, LENGTH);
	
	mergeSort(array, 0, LENGTH, dstArray);	
	printArray(dstArray, LENGTH);
	return 0;
}
