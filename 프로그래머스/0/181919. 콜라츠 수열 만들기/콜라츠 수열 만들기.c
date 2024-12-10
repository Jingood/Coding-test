#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int n) {
    int cnt = 0;
    int* answer = (int*)malloc(1000 * sizeof(int));
    while(n)
    {
        answer[cnt] = n;
        if(n == 1)
            break;
        if(!(n % 2))
        {
            n /= 2;
            cnt++;
        }
        else if(n % 2)
        {
            n = 3 * n + 1;
            cnt++;
        }
    }
    answer = (int*) realloc(answer, (cnt+1) * sizeof(int));
    return answer;
}