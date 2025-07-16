import java.io.*;

public class BOJ2018 {
    public static void main(String[] args) throws IOException {
        var bf = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bf.readLine());
        
        var sum = 1;
        var startIndex = 1;
        var endIndex = 1;
        var result = 1;

        while(endIndex != N) {
            if(sum == N) {
                result += 1;
                endIndex += 1;
                sum += endIndex;
            } else if (sum < N) {
                endIndex += 1;
                sum += endIndex;
            } else {
                sum -= startIndex;
                startIndex += 1;
            }
        }
        System.out.println(result);
    }
}
