#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(const char* my_string, const char* is_suffix) {
    int len = strlen(my_string);
    int cnt = 0;
    int answer = 0;
    for(int i=0 ; i<len ; i++) {
        if(!strcmp(my_string + i, is_suffix))
            cnt++;
    }
    if(!cnt)
        answer = 0;
    else
        answer = 1;
    return answer;
}