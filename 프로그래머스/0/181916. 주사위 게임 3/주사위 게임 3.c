#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int a, int b, int c, int d) {
    int arr[4] = {a, b, c, d};
    int count[7] = {0}; // 1~6 주사위 값의 빈도수 저장
    int same_value = -1; // 같은 값 중 가장 높은 빈도수를 가진 값
    int different_values[2]; // 서로 다른 값 저장
    int majority_count = 0; // 가장 많은 값의 빈도수
    int different_count = 0; // 서로 다른 값의 개수
    int answer = 0;

    // 주사위 값 빈도수 계산
    for (int i = 0; i < 4; i++) {
        count[arr[i]]++;
    }

    // 값의 빈도수 기반으로 분석
    for (int i = 1; i <= 6; i++) {
        if (count[i] > majority_count) {
            same_value = i;
            majority_count = count[i];
        }
        if (count[i] == 1) {
            different_values[different_count++] = i;
        }
    }

    // 조건에 따른 결과 계산
    if (majority_count == 4) {
        answer = 1111 * same_value; // 모든 값이 같을 경우
    } else if (majority_count == 3) {
        for (int j = 1; j <= 6; j++) {
            if (count[j] == 1) {
                answer = (10 * same_value + j) * (10 * same_value + j);
                break;
            }
        }
    } else if (majority_count == 2) {
        int pair_count = 0; // 2번 등장한 값의 개수
        int pairs[2];       // 두 번 등장한 값 저장
        for (int j = 1; j <= 6; j++) {
            if (count[j] == 2) {
                pairs[pair_count++] = j;
            }
        }
        if (pair_count == 2) { // 둘 둘씩 같은 경우
            answer = (pairs[0] + pairs[1]) * abs(pairs[0] - pairs[1]);
        } else { // 한 값만 두 번 등장한 경우
            answer = different_values[0] * different_values[1];
        }
    } else if (different_count == 4) {
        int is_min = arr[0];
        for (int i = 1; i < 4; i++) {
            if (arr[i] < is_min)
                is_min = arr[i];
        }
        answer = is_min; // 모든 값이 다른 경우 최솟값
    }

    return answer;
}
