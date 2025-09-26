class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        int len = numbers.length;
        for (int number : numbers) {
            answer += number;
        }
        return answer / len;
    }
}