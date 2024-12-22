#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

int compare(const void* a, const void* b) {
    return strcmp(*(const char**)a, *(const char**)b);
}

char** solution(const char* my_string) {
    int len = strlen(my_string);
    char** answer = (char**)malloc(len * sizeof(char*));
    for(int i=0 ; i<len ; i++) {
        answer[i] = (char*)malloc((len - i + 1) * sizeof(char));
        strcpy(answer[i], my_string + i);
    }
    qsort(answer, len, sizeof(char*), compare);
    return answer;
}