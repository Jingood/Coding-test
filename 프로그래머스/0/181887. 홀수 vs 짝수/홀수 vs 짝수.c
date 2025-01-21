#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int num_list[], size_t num_list_len) {
    int answer = 0;
    int odd = 0, twice = 0;
    for(int i=0 ; i<num_list_len ; i++) {
        if(!(i % 2))
            odd += num_list[i];
        else if(i % 2)
            twice += num_list[i];
    }
    if(odd > twice)
        answer = odd;
    else
        answer = twice;
    return answer;
}