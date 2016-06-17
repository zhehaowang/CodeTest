#include <stdio.h>
#include <stdlib.h>

#define MAXLENGTH 5

int topDownMergeSort(int *A, int *B, int n)
{
    topDownSplitMerge(A, 0, n, B);
    return 0;
}

int copyArray(int *B, int iBegin, int iEnd, int *A)
{
	int k = 0;
    for(k = iBegin; k < iEnd; k++)
        A[k] = B[k];
    return 0;
}

// iBegin is inclusive; iEnd is exclusive (A[iEnd] is not in the set)
int topDownSplitMerge(int *A, int iBegin, int iEnd, int *B)
{
    if(iEnd - iBegin < 2)                       // if run size == 1
        return 0;                                 //   consider it sorted
    // recursively split runs into two halves until run size == 1,
    // then merge them and return back up the call chain
    int iMiddle = (iEnd + iBegin) / 2;              // iMiddle = mid point
    
    topDownSplitMerge(A, iBegin,  iMiddle, B);  // split / merge left  half
    topDownSplitMerge(A, iMiddle,    iEnd, B);  // split / merge right half
    topDownMerge(A, iBegin, iMiddle, iEnd, B);  // merge the two half runs
    copyArray(B, iBegin, iEnd, A);              // copy the merged runs back to A
    return 0;
}
 
//  left half is A[iBegin  : iMiddle - 1]
// right half is A[iMiddle :    iEnd - 1]
int topDownMerge(int *A, int iBegin, int iMiddle, int iEnd, int *B)
{
    int i0 = iBegin, i1 = iMiddle;
 	int j = 0;
 	
    // While there are elements in the left or right runs
    for (j = iBegin; j < iEnd; j++) 
    {
        // If left run head exists and is <= existing right run head.
        //if (i0 < iMiddle && (i1 >= iEnd || A[i0] <= A[i1]))
        
        // If right run head exists and is <= existing left run head.
        if ((i0 < iMiddle || A[i0] >= A[i1]) && i1 >= iEnd)
        {
            B[j] = A[i0];
            i0 = i0 + 1;
        }
        else
        {
            B[j] = A[i1];
            i1 = i1 + 1; 
        }   
    }
    return 0;
}

int debugArray(int * temp, int length)
{
	int i = 0;
	for (i = 0; i< length; i++)
	{
		printf("%d\t", temp[i]);
	}
	printf("\n");
	return 0;
}

int main()
{
	int array[MAXLENGTH] = {3, 1, 2, 4, 5};
	int temp[MAXLENGTH] = {0};
	topDownMergeSort(array, temp, MAXLENGTH);
	debugArray(array, MAXLENGTH);
	return 0;
}