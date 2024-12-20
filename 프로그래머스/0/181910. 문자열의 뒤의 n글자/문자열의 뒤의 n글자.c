#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(const char* my_string, int n) {
    int len = strlen(my_string);
    char* answer = (char*)malloc(n + 1);
    if(answer == NULL)
        return NULL;
    strncpy(answer, my_string + (len - n), n);
    answer[n] = 0;
    return answer;
}