import java.util.*;
import java.io.*;

public class BOJ11720 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bf.readLine());
        String number = bf.readLine();
        char[] numberArr = number.toCharArray();
        int answer = 0;

        for (int i = 0; i < n; i++) {
             answer += Character.getNumericValue(numberArr[i]);
        }
        System.out.println(answer);
    }
}
