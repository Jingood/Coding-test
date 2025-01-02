#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int start_num, int end_num) {
    int idx = 0;
    int* answer = (int*)malloc((start_num - end_num + 1) * sizeof(int));
    if(answer == NULL)
        return NULL;
    for(int i=start_num ; i >= end_num ; i--)
        answer[idx++] = i;
    return answer;
}