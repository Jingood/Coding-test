#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(int q, int r, const char* code) {
    int len = strlen(code);
    int relen = 0;
    char* answer = (char*)malloc(len + 1);
    answer[len] = 0;
    for(int i=0 ; i<len ; i++)
    {
        if(i % q == r)
            answer[relen++] = code[i];
    }
    answer = (char*)realloc(answer, relen + 1);
    answer[relen] = 0;
    return answer;
}