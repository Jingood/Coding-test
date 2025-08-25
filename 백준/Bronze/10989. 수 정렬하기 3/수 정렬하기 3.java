import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


// 일정한 수를 입력받고 이를 오름차순 정렬하는 함수
public class Main {
    public static void main(String[] args) throws IOException {
        // 수의 범위 (0 ~ 10000) 사실 상 0은 제외
        int[] cnt = new int[10001];

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        for (int i=0 ; i<N ; i++) {
            // 해당 인덱스의 값 1 증가
            cnt[Integer.parseInt(br.readLine())] ++;
        }

        br.close();

        StringBuilder sb = new StringBuilder();

        // 0은 입력 범위에서 제외이므로 1부터 시작
        for (int i=1 ; i<10001 ; i++) {
            while (cnt[i] > 0) {
                sb.append(i).append('\n');
                cnt[i]--;
            }
        }
        System.out.println(sb);
    }
}
