#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int arr[], size_t arr_len) {
    int* answer = (int*)malloc(arr_len * sizeof(int));
    int adx = 0;
    for(int i=0 ; i<arr_len ; i++) {
        if((arr[i] >= 50) && !(arr[i] % 2))
            answer[adx++] = arr[i] / 2;
        else if((arr[i] < 50) && (arr[i] % 2))
            answer[adx++] = arr[i] * 2;
        else
            answer[adx++] = arr[i];
    }
    return answer;
}