#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(const char* rny_string) {
    int i, j = 0;
    int len = 0;
    int r_len = strlen(rny_string);
    for(i=0 ; i<r_len ; i++)
    {
        if(rny_string[i] == 'm')
            len += 2;
        else
            len++;
    }
    char* answer = (char*)malloc(len+1);
    for(i=0 ; i<r_len ; i++)
    {
        if(rny_string[i] == 'm')
        {
            answer[j++] = 'r';
            answer[j++] = 'n';
        }
        else
            answer[j++] = rny_string[i];
    }
    answer[j]='\0';
    return answer;
}