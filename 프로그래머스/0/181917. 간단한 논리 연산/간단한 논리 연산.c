#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(bool x1, bool x2, bool x3, bool x4) {
    bool a = true, b = true;
    bool answer = true;
    if(!x1 && !x2)
        a = false;
    if(!x3 && !x4)
        b = false;
    if(!a || !b)
        answer = false;
    return answer;
}