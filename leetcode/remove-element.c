int removeElement(int A[], int n, int elem) {
    int i = 0;
    int total = n;
    
    while (total > i) {
        if (A[i] == elem) {
            total --;
            while (total > i && A[total] == elem) {
                total--;
            }
            if (total == i) {
                return total;
            }
            A[i] = A[total];
        }
        i++;
    }
    
    return total;
}

int main() {
    int A[5] = {3, 3, 3, 3, 3};
    int i = removeElement(A, 5, 3);
    for (int j = 0; j < i; j++) {
        printf("%d\n", A[j]);
    }
}
