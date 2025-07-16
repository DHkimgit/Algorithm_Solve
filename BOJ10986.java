import java.util.*;
import java.io.*;

public class BOJ10986 {
    public static void main(String[] args) throws IOException {
        var bf = new BufferedReader(new InputStreamReader(System.in));
        var st = new StringTokenizer(bf.readLine());
        
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        long[] S = new long[N + 1];
        st = new StringTokenizer(bf.readLine());

        for(int i = 1; i < N + 1; i++) {
            S[i] = S[i - 1] + Integer.parseInt(st.nextToken());
        }

        long result = 0;
        long[] index = new long[M];

        for(int i = 1; i < N + 1; i++) {
            int r = (int) (S[i] % M);
            if (r == 0) result += 1;
            index[r] += 1;
        }

        for(int i = 0; i < M; i++) {
            if(index[i] > 1) {
                result += (index[i] * (index[i] - 1)) / 2; 
            }
        }
        System.out.println(result);
    }
}
