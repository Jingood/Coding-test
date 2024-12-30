#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(const char* my_string) {
    int len = strlen(my_string);
    int* answer = (int*)calloc(52, sizeof(int));
    if(answer == NULL)
        return NULL;
    for(int i=0 ; i<len ; i++)
    {
        char c = my_string[i];
        if(c >= 'A' && c <= 'Z')
            answer[c - 'A'] += 1;
        else if(c >= 'a' && c <= 'z')
            answer[c - 'a' + 26] += 1;
    }
    return answer;
}