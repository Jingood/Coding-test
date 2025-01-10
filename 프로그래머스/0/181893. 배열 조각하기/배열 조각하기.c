#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int arr[], size_t arr_len, int query[], size_t query_len) {
    int start = 0;
    int end = arr_len - 1;
    for(int i=0 ; i<query_len ; i++) {
        if(i % 2 == 0)
            end = start + query[i];
        else if(i % 2 != 0)
            start = start + query[i];
    }
    int len = end - start + 1;
    int* answer = (int*)malloc(len * sizeof(int));
    if(answer == NULL)
        return NULL;
    for(int j=0 ; j<len ; j++)
        answer[j] = arr[start + j];
    return answer;
}