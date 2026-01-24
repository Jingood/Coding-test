import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] counts = new int[10];

        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();
        sc.nextLine();

        int rs = A * B * C;

        if(rs ==0) {
            counts[0]++;
        } else {
            while (rs > 0) {
                int digit = rs % 10;
                counts[digit]++;
                rs /= 10;
            }
        }

        for (int i = 0; i < counts.length; i++) {
            System.out.println(counts[i]);
        }
    }
}
