#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int arr[], size_t arr_len, int** intervals, size_t intervals_rows, size_t intervals_cols) {
    int len = (intervals[0][1] - intervals[0][0] + 1) + (intervals[1][1] - intervals[1][0] + 1);
    int cnt = 0;
    int* answer = (int*)malloc(len * sizeof(len));
    for(int i=0 ; i<intervals_rows ; i++)
        for(int j=intervals[i][0] ; j<=intervals[i][1] ; j++) {
            answer[cnt++] = arr[j];
        }
    answer = (int*)realloc(answer, cnt * sizeof(int));
    return answer;
}