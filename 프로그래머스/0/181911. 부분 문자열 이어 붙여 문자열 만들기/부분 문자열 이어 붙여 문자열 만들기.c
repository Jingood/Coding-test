#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(const char* my_strings[], size_t my_strings_len, int** parts, size_t parts_rows, size_t parts_cols) {
    int len = 0;
    for(int i=0 ; i<parts_rows ; i++)
        len += (parts[i][1] - parts[i][0] + 1);
    char* answer = (char*)malloc(len + 1);
    if(answer == NULL)
        return NULL;
    answer[0] = '\0';
    for(int i=0 ; i<parts_rows ; i++)
    {
        int s = parts[i][0];
        int e = parts[i][1];
        int t_len = e - s + 1;
        char temp[t_len];
        temp[t_len] = 0;
        strncpy(temp, my_strings[i] + s, t_len);
        strcat(answer, temp);
    }
    return answer;
}