#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int n, int k) {
    int len = n / k;
    int cnt = 0;
    int* answer = (int*)malloc(len * sizeof(int));
    for(int i=1 ; i<=n ; i++)
    {
        if(i % k == 0) {
            answer[cnt] = i;
            cnt++;
        }
    }
    return answer;
}