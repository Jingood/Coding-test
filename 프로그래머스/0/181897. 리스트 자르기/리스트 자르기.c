#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int n, int slicer[], size_t slicer_len, int num_list[], size_t num_list_len) {
    int* answer = (int*)calloc(num_list_len, sizeof(int));
    if (!answer) return NULL;

    int start, end, gap, cnt = 0;

    if (n == 1) {
        end = slicer[1];
        for (int i = 0; i <= end && i < num_list_len; i++) {
            answer[i] = num_list[i];
            cnt++;
        }
    } else if (n == 2) {
        start = slicer[0];
        for (int i = start; i < num_list_len; i++) {
            answer[cnt++] = num_list[i];
        }
    } else if (n == 3) {
        start = slicer[0];
        end = slicer[1];
        for (int i = start; i <= end && i < num_list_len; i++) {
            answer[cnt++] = num_list[i];
        }
    } else {
        start = slicer[0];
        end = slicer[1];
        gap = slicer[2];
        for (int i = 0; start <= end && start < num_list_len; i++) {
            answer[cnt++] = num_list[start];
            start += gap;
        }
    }

    int* temp = realloc(answer, cnt * sizeof(int));
    if (!temp) {
        free(answer);
        return NULL;
    }
    return temp;
}
