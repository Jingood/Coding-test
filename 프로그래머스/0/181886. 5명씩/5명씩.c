#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char** solution(const char* names[], size_t names_len) {
    int len = (names_len + 4) / 5; 
    int aidx = 0;
    char** answer = (char**)malloc((len + 1) * sizeof(char *));
    for(int i=0 ; i<names_len ; i += 5) {
        answer[aidx++] = names[i];
    }
    return answer;
}