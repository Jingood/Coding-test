#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int num_list[], size_t num_list_len, int n) {
    int idx = 0;
    int* answer = (int*)malloc(num_list_len * sizeof(int));
    for(int i=n ; i<num_list_len ; i++)
        answer[idx++] = num_list[i];
    for(int i=0 ; i<n ; i++)
        answer[idx++] = num_list[i];
    return answer;
}