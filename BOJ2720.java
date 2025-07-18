import java.io.*;

public class BOJ2720 {
    public static void main(String[] args) throws IOException {
        var bf = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(bf.readLine());
        int[] maps = {25, 10, 5, 1};

        for (int i = 0; i < T; i++) {
            StringBuilder sb = new StringBuilder();
            int C = Integer.parseInt(bf.readLine());

            for (int j = 0; j < 4; j++) {
                int result = C / maps[j];
                sb.append(result).append(" ");
                C = C - (result * maps[j]);
            }
            System.out.println(sb);
        }
    }
}
