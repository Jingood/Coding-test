#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int num_list[], size_t num_list_len, int n) {
    int len = num_list_len - n + 1;
    int idx = 0;
    int* answer = (int*)malloc(len * sizeof(int));
    for(int i=n-1 ; i<num_list_len ; i++)
        answer[idx++] = num_list[i];
    return answer;
}