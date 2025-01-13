#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char** solution(const char* str_list[], size_t str_list_len) {
    int idx = -1;
    char firstChar = '\0';
    for(int i=0 ; i<str_list_len ; i++) {
        if(!(strcmp(str_list[i], "l"))) {
            idx = i;
            firstChar = 'l';
            break;
        }
        else if(!(strcmp(str_list[i], "r"))) {
            idx = i;
            firstChar = 'r';
            break;
        }
    }
    if(idx == -1) {
        char** answer = (char**)malloc(sizeof(char*));
        if(answer == NULL)
            return NULL;
        answer[0] = NULL;
        return answer;
    }
    
    if(firstChar == 'l') {
        int leftCount = idx;
        char** answer = (char**)malloc(sizeof(char*) * (leftCount + 1));
        if(answer == NULL)
            return NULL;
        for(int i=0 ; i<leftCount ; i++) {
            int len = strlen(str_list[i]);
            answer[i] = (char*)malloc(len + 1);
            strcpy(answer[i], str_list[i]);
        }
        answer[leftCount] = NULL;
        return answer;
    }
    
    else if(firstChar == 'r') {
        int rightCount = str_list_len - (idx + 1);
        char** answer = (char**)malloc(sizeof(char*) * (rightCount + 1));
        if(answer == NULL)
            return NULL;
        for(int i=0 ; i<rightCount ; i++) {
            int originalIdx = idx + 1 + i;
            int len = strlen(str_list[originalIdx]);
            answer[i] = (char*)malloc(len + 1);
            strcpy(answer[i], str_list[originalIdx]);
        }
        answer[rightCount] = NULL;
        return answer;
    }
}