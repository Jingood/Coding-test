#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int num_list[], size_t num_list_len) {
    int answer = 0;
    int ans = 1;
    for(int i=0 ; i<num_list_len ; i++) {
        if(num_list_len >= 11)
            answer += num_list[i];
        else if(num_list_len <= 10) 
            ans = ans * num_list[i];
    }
    if(ans != 1)
        answer = ans;
    return answer;
}