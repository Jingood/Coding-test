#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(const char* number) {
    int len = strlen(number);
    int add = 0;
    for(int i=0 ; i<len ; i++) 
         add += number[i] - '0';
    return add % 9;
}