#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int to_lower(char c) {
    return ('A' <= c && c <= 'Z') ? c + ('a' - 'A') : c;
}

int solution(const char* myString, const char* pat) {
    int myLen = strlen(myString);
    int patLen = strlen(pat);

    if (myLen < patLen)
        return 0;

    for (int i = 0; i <= myLen - patLen; i++) {
        bool found = true;
        for (int j = 0; j < patLen; j++) {
            if (to_lower(myString[i + j]) != to_lower(pat[j])) {
                found = false;
                break;
            }
        }
        if (found)
            return 1;
    }

    return 0;
}
