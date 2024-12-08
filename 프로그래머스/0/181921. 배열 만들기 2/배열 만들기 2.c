#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool is_valid_num(int i)
{
    while(i > 0)
    {
        int digit = i % 10;
        if(digit != 5 && digit)
            return false;
        i /= 10;
    }
    return true;
}

int* solution(int l, int r) {
    int i, c=0, t=0;
    for(i=l ; i<=r ; i++)
    {
        if(is_valid_num(i))
            c++;
    }
    if(!c)
        c = 1;
    int* answer = (int*)malloc(c * (sizeof(int)));
    for(i=l ; i<=r ; i++)
    {
        if(is_valid_num(i))
        {
            answer[t] = i;
            t++;
        }
    }
    if(!t)
        answer[t] = -1;
    return answer;
}