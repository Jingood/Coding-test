#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* solution(const char* my_string, const char* alp) {
    int mylen = strlen(my_string);
    int diff = 'a' - 'A';
    char* answer = (char*)malloc(mylen + 1);
    if(answer == NULL)
        return NULL;
    strcpy(answer, my_string);
    for(int i=0 ; i<mylen ; i++) {
        if(answer[i] == alp[0])
            answer[i] -= diff;
    }
    return answer;
}