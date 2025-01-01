#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

int compare(const void* a, const void* b)
{
    return (*(int*)a - *(int*)b);
}
char* solution(const char* my_string, int indices[], size_t indices_len) {
    int len = strlen(my_string) - indices_len;
    int aidx = 0;
    char* answer = (char*)malloc(len + 1);
    if(answer == NULL)
        return NULL;
    qsort(indices, indices_len, sizeof(int), compare);
    int iidx = 0;
    for(int i=0 ; i<strlen(my_string) ; i++) {
        if(iidx < indices_len && i == indices[iidx])
            iidx++;
        else
            answer[aidx++] = my_string[i];
    }
    answer[len] = 0;
    return answer;
}