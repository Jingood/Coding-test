#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(const char* intStrs[], size_t intStrs_len, int k, int s, int l) {
    int intcomp;
    int len = 0;
    int* answer = (int*)malloc(intStrs_len * sizeof(int));
    if(answer == NULL)
        return NULL;
    for(int i=0 ; i<intStrs_len ; i++)
    {
        char comp[9] = {0};
        strncpy(comp, intStrs[i] + s, l);
        intcomp = atoi(comp);
        if(intcomp > k)
            answer[len++] = intcomp;
    }
    answer = (int *)realloc(answer, len * sizeof(int));
    return answer;
}