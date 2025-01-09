#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int arr[], size_t arr_len) {
    int cnt = 0;
    int idx = 0;
    int* answer = (int*)malloc(arr_len * sizeof(int));
    for(int i=0 ; i<arr_len ; i++) {
        if(arr[i] == 2)
            cnt++;
    }
    if(!cnt) {
        answer = (int*)realloc(answer, sizeof(int));
        answer[0] = -1;
        return answer;
    }
    
    int* temp = (int*)malloc(cnt * sizeof(int));
    int aidx = 0;
    for(int j=0 ; j<arr_len ; j++) {
        if(arr[j] == 2)
            temp[idx++] = j;
    }
    for(int k=temp[0] ; k<=temp[cnt - 1] ; k++) {
        answer[aidx++] = arr[k];
    }
    free(temp);
    answer = (int*)realloc(answer, aidx * sizeof(int));
    return answer;
}