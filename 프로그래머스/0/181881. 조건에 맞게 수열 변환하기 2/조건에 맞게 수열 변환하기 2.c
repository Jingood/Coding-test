#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int stableSteps[101];

int getStableSteps(int e) {
    int step = 0;
    int current = e;
    while(1) {
        int next = current;
        
        if(current >= 50 && !(current % 2))
            next = current / 2;
        else if(current < 50 && (current % 2))
            next = current * 2 + 1;
        
        if(next == current)
            return step;
        
        current = next;
        step++;
    }
}


int solution(int arr[], size_t arr_len) {
    int answer = 0;
    
    for(int i=1 ; i<=100 ; i++) {
        stableSteps[i] = getStableSteps(i);
    }
    
    for(int i=0 ; i<arr_len ; i++) {
        if(stableSteps[arr[i]] > answer)
            answer = stableSteps[arr[i]];
    }
    return answer;
}