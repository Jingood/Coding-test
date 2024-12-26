#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(const char* my_string, const char* is_prefix) {
    int len = strlen(my_string);
    int cnt = 0;
    int answer = 0;
    for(int i=1 ; i<len + 1 ; i++) {
        char temp[i+1];
        strncpy(temp, my_string, i);
        temp[i] = 0;
        if(!strcmp(temp, is_prefix))
            cnt++;
    }
    if(!cnt)
        answer = 0;
    else
        answer = 1;
    return answer;
}