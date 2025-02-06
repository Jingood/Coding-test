#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* solution(const char* myString) {
    int mylen = strlen(myString);
    int diff = 'a' - 'A';
    char* answer = (char*)malloc(mylen + 1);
    if(answer == NULL)
        return NULL;
    strcpy(answer, myString);
    for(int i=0 ; i<mylen ; i++) {
        if(answer[i] == 'a')
            answer[i] -= diff;
        else if(answer[i] >= 'B' && answer[i] <= 'Z')
            answer[i] += diff;
    }
    answer[mylen] = '\0';
    return answer;
}