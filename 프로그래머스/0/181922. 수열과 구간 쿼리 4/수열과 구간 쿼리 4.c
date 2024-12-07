#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int arr[], size_t arr_len, int** queries, size_t queries_rows, size_t queries_cols) {
    int i, j, l, s, e, k;
    int* answer = (int*)malloc(arr_len * sizeof(int));
    for(i=0 ; i<arr_len ; i++)
        answer[i] = arr[i];
    for(j=0 ; j<queries_rows ; j++)
    {
        s = queries[j][0];
        e = queries[j][1];
        k = queries[j][2];
        for(l=s ; l<=e ; l++)
        {
            if(!l || !(l % k))
                answer[l]++;
        }
    }
    return answer;
}