#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char** solution(const char* todo_list[], size_t todo_list_len, bool finished[], size_t finished_len) {
    int len = 0;
    int aidx = 0;
    for(int i=0 ; i<finished_len ; i++) {
        if(!finished[i])
            len++;
    }
    char** answer = (char**)malloc((len + 1) * sizeof(char *));
    if(answer == NULL)
        return NULL;
    for(int i=0 ; i<todo_list_len ; i++) {
        if(!finished[i])
            answer[aidx++] = todo_list[i];
    }
    return answer;
}