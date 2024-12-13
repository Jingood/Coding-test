#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>


char* solution(const char* my_string, int index_list[], size_t index_list_len) {
    int i;
    char* answer = (char*)malloc(index_list_len + 1);
    for(i=0 ; i<index_list_len ; i++)
    {
        answer[i] = my_string[index_list[i]];
    }
    answer[i]=0;
    return answer;
}