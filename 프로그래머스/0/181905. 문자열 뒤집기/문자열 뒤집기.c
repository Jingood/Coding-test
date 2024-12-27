#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(const char* my_string, int s, int e) {
    int len = strlen(my_string);
    char* answer = (char*)malloc(len + 1);
    if(answer == NULL)
        return NULL;
    answer[len] = 0;
    strcpy(answer, my_string);
    for(int i=0 ; i<(e - s + 1)/2 ; i++) {
        char temp = answer[s + i];
        answer[s + i] = answer[e - i];
        answer[e - i] = temp;
    }
    return answer;
}