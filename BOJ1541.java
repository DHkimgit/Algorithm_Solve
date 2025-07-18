import java.io.*;
import java.util.*;

public class BOJ1541 {
    public static void main(String[] args) throws IOException {
        var bf = new BufferedReader(new InputStreamReader(System.in));
        var st = new StringTokenizer(bf.readLine(), "-");
        int result = Integer.MAX_VALUE;

        while (st.hasMoreTokens()) {
            int tmp = 0;
            
            var add = new StringTokenizer(st.nextToken(), "+");

            while (add.hasMoreTokens()) {
                tmp += Integer.parseInt(add.nextToken());
            }

            if (result == Integer.MAX_VALUE) {
                result = tmp;
            } else {
                result -= tmp;
            }
        }

        System.out.println(result);
    }
}
