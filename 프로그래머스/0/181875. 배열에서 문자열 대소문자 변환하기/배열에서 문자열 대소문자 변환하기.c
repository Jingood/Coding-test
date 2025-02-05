#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char** solution(const char* strArr[], size_t strArr_len) {
    int diff = 'a' - 'A';
    char** answer = (char**)malloc((strArr_len + 1) * sizeof(char *));
    if(answer == NULL)
        return NULL;
    for(int i=0 ; i<strArr_len ; i++) {
        int len = strlen(strArr[i]);
        answer[i] = malloc((len + 1) * sizeof(char));
        strcpy(answer[i], strArr[i]);
        for(int j=0 ; j<len ; j++) {
            if(!(i % 2)) {
                if(answer[i][j] >= 'A' && answer[i][j] <= 'Z')
                    answer[i][j] += diff;
            }
            else {
                if(answer[i][j] >= 'a' && answer[i][j] <= 'z')
                    answer[i][j] -= diff;
            }
        }
    }
    answer[strArr_len] = '\0';
    return answer;
}