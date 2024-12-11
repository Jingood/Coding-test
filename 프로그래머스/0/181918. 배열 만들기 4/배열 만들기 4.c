#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int arr[], size_t arr_len) {
    int i = 0, cnt = 0;
    int* stk = (int*)calloc(arr_len, sizeof(int));
    while(i<arr_len)
    {
        if(!cnt || stk[cnt - 1] < arr[i])
            stk[cnt++] = arr[i++];
        else
            cnt--;
    }
    stk = (int *)realloc(stk, cnt * sizeof(int));
    return stk;
}