import java.util.*;
import java.io.*;

public class BOJ11660 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        long[][] S = new long[N + 1][N + 1];

        for (int i = 1; i < N + 1; i++) {
            st = new StringTokenizer(bf.readLine());
            S[i][1] = Integer.parseInt(st.nextToken());
            for (int j = 2; j < N + 1; j++) {
                S[i][j] = S[i][j - 1] + Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(bf.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());
            long result = 0;
            for (int j = x1; j < x2 + 1; j++) {
                result += S[j][y2] - S[j][y1 - 1];
            }
            sb.append(result).append('\n');
        }
        System.out.println(sb);
    }
}
