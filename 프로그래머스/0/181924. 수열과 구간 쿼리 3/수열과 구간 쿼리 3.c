#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int arr[], size_t arr_len, int** queries, size_t queries_rows, size_t queries_cols) {
    int i, j, k, l, temp;
    int* answer = (int*)malloc((arr_len + 1) * sizeof(int));
    for(i-0 ; i<arr_len ; i++)
        answer[i] = arr[i];
    for(j=0 ; j<queries_rows ; j++)
    {
        k = queries[j][0];
        l = queries[j][1];
        temp = answer[k];
        answer[k] = answer[l];
        answer[l] = temp;
    }
    return answer;
}