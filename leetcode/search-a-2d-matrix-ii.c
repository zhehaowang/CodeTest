#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool searchMatrix(int (*matrix)[3], int matrixRowSize, int matrixColSize, int target) {
    int i = 0, j = 0;
    int upBound = 0, downBound = 0, leftBound = 0, rightBound = 0;
    
    for (i = 0; i < matrixColSize; i++) {
        if (matrix[matrixRowSize - 1][i] < target) {
            leftBound ++;
        }
    }

    for (i = matrixColSize - 1; i >= 0; i--) {
        if (matrix[0][i] > target) {
            rightBound ++;
        }
    }
    rightBound = matrixColSize - rightBound;
    
    for (i = 0; i < matrixRowSize; i++) {
        if (matrix[i][matrixColSize - 1] < target) {
            upBound ++;
        }
    }
    for (i = matrixRowSize - 1; i >= 0; i--) {
        if (matrix[i][0] > target) {
            downBound ++;
        }
    }
    downBound = matrixRowSize - downBound;

    for (i = leftBound; i < rightBound; i++) {
        for (j = upBound; j < downBound; j++) {
            if (matrix[j][i] == target) {
                return true;
            }
            if (matrix[j][i] > target) {
                break;
            }
        }
    }
    
    return false;
}

int main() {
    int matrix[5][3] = {1, 4, 9, 4, 6, 12, 9, 13, 15, 10, 14, 15, 11, 16, 20};
    printf("%d\n", searchMatrix(matrix, 5, 3, 5));
}