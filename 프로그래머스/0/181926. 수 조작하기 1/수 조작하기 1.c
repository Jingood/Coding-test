#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n, const char* control) {
    int i;
    int len = strlen(control);
    for(i=0 ; i<len ; i++)
    {
        if(control[i] == 'w')
            n += 1;
        else if(control[i] == 's')
            n -= 1;
        else if(control[i] == 'd')
            n += 10;
        else if(control[i] == 'a')
            n -= 10;
    }
    return n;
}