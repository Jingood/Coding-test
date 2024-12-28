#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>


char* solution(const char* my_string, int m, int c) {
    int mylen = strlen(my_string);
    int aslen = mylen / m;
    int i = c - 1;
    int cnt = 0;
    char* answer = (char*)malloc(aslen + 1);
    if(answer == NULL)
        return NULL;
    answer[aslen] = 0;
    while(cnt < aslen)
    {
        answer[cnt] = my_string[i];
        cnt++;
        i += m;
    }
    return answer;
}