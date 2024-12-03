#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(int numLog[], size_t numLog_len) {
    int i;
    char* answer = (char*)malloc(numLog_len);
    strcpy(answer, "\0");
    for(i=1 ; i<numLog_len ; i++)
    {
        if(numLog[i] == numLog[i-1] + 1)
            strcat(answer, "w");
        else if(numLog[i] == numLog[i-1] - 1)
            strcat(answer, "s");
        else if(numLog[i] == numLog[i-1] + 10)
            strcat(answer, "d");
        else if(numLog[i] == numLog[i-1] - 10)
            strcat(answer, "a");
    }
    return answer;
}