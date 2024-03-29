#include <stdio.h>
#include <stdlib.h>

void multiply(int fibMat[2][2], int multMat[2][2]);
void power(int fibMat[2][2], int n);

// Fibonacci as recursion
int fib1(int n) {
    if(n == 0) return 0;
    if(n == 1) return 1;
    return fib1(n - 1) + fib1(n - 2);
}

// Fibonacci as a polynomial
int fib2(int n) {
    if(n == 0) return 0;
    int* fList = malloc((n + 1)*sizeof(int));
    fList[0] = 0;
    fList[1] = 1;
    int i;
    for(i = 2; i <= n + 1; i++) {
        fList[i] = fList[i - 1] + fList[i - 2];
    }
    return fList[n];
}

// Fibonacci in matrix form
// Time Complexity: O(logn)
int fib3(int n) {
    if(n == 0) return 0;
    if(n == 1) return 1;
    int fibMat[2][2] = {{0, 1}, {1, 1}};
    power(fibMat, n - 1);
    return fibMat[0][0];
}

void power(int fibMat[2][2], int n) {
    int i;
    int multMat[2][2] = {{0, 1}, {1, 1}};
    for(i = 0; i <= n; i++) {
        multiply(fibMat, multMat);
    }
}

void multiply(int fibMat[2][2], int multMat[2][2]) {
    int topLeft = fibMat[0][0]*multMat[0][0] + fibMat[0][1]*multMat[1][0];
    int topRight = fibMat[0][0]*multMat[0][1] + fibMat[0][1]*multMat[1][1];
    int bottomLeft = fibMat[1][0]*multMat[0][0] + fibMat[1][1]*multMat[1][0];
    int bottomRight = fibMat[1][0]*multMat[0][1] + fibMat[1][1]*multMat[1][1];
    fibMat[0][0] = topLeft;
    fibMat[0][1] = topRight;
    fibMat[1][0] = bottomLeft;
    fibMat[1][1] = bottomRight;
}

int main() {
    printf("By recursion: %d\n", fib1(8));
    printf("By polynomial: %d\n", fib2(8));
    printf("By matrices: %d", fib3(8));
    return 0;
}