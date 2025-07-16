import java.io.*;
import java.util.*;

public class BOJ2750 {
    public static void main(String args[]) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(bf.readLine());
        int[] arr = new int[10001];

        for (int i = 0; i < n; i++) {
            arr[Integer.parseInt(bf.readLine())] += 1;
        }
        
        for (int i = 0; i < 10001; i++) {
            if(arr[i] > 0) {
                for (int j = 0; j < arr[i]; j++) {
                    sb.append(i).append('\n');
                }
            }
        }
        System.out.println(sb);
    }
}
