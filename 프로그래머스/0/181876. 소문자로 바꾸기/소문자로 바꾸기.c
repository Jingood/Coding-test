#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

char* solution(const char* myString) {
    int mylen = strlen(myString);
    int diff = 'a' - 'A';
    char* answer = (char*)malloc(mylen + 1);
    if(answer == NULL)
        return NULL;
    answer[mylen] = '\0';
    strcpy(answer, myString);
    for(int i=0 ; i<mylen ; i++) {
        if(answer[i] >= 'A' && answer[i] <= 'Z')
            answer[i] += diff;
    }
    return answer;
}