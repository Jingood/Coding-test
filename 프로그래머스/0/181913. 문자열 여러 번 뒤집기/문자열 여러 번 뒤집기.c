#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(const char* my_string, int** queries, size_t queries_rows, size_t queries_cols) {
    int len = strlen(my_string);
    char* answer = (char*)malloc(len + 1);
    strcpy(answer, my_string);
    char temp;
    for(int i=0 ; i<queries_rows ; i++)
    {   
        int s = queries[i][0];
        int e = queries[i][1];
        for(int j=0 ; j<(e - s + 1)/2 ; j++)
        {
            temp = answer[s + j];
            answer[s + j] = answer[e - j];
            answer[e - j] = temp;
        }
    }
    return answer;
}