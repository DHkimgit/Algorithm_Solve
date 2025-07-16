import java.io.*;
import java.util.*;

public class BOJ1940 {
    public static void main(String[] args) throws IOException {
        var bf = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bf.readLine());
        int M = Integer.parseInt(bf.readLine());

        var st = new StringTokenizer(bf.readLine());
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);
        int startPointer = 0;
        int endPointer = N - 1;
        int result = 0;

        while(startPointer != endPointer) {
            if(arr[startPointer] + arr[endPointer] == M) {
                result += 1;
                endPointer -= 1;
            } else if(arr[startPointer] + arr[endPointer] < M) {
                startPointer += 1;
            } else {
                endPointer -= 1;
            }
        }
        System.out.println(result);
    }
}
