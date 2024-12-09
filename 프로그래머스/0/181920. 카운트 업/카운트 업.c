#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int start_num, int end_num) {
    int len = end_num - start_num;
    int i, j=0;
    int* answer = (int*)malloc((len + 1) * sizeof(int));
    for(i=start_num ; i<end_num+1 ; i++)
    {
        answer[j]=i;
        j++;
    }
    return answer; 
}