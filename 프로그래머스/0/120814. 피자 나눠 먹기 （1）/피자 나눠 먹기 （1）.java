class Solution {
    public int solution(int n) {
        int answer = 0;
        
        if (7 > n) {
            answer = 1;
        } else if (n % 7 != 0) {
            answer = n / 7 + 1;
        } else {
            answer = n / 7;
        }
        return answer;
    }
}