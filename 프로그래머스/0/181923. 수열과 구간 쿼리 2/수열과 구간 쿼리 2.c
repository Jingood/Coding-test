#include <stdio.h>
#include <stdlib.h>
#include <limits.h> 

int* solution(int arr[], size_t arr_len, int** queries, size_t queries_rows, size_t queries_cols) {
    int* answer = (int*)malloc(queries_rows * sizeof(int));
    for (int i = 0; i < queries_rows; i++) {
        int s = queries[i][0]; 
        int e = queries[i][1]; 
        int k = queries[i][2]; 

        int min_value = INT_MAX;

        for (int j = s; j <= e; j++) {
            if (arr[j] > k && arr[j] < min_value) {
                min_value = arr[j];
            }
        }

        if (min_value == INT_MAX) {
            answer[i] = -1;
        } else {
            answer[i] = min_value;
        }
    }
    return answer;
}
