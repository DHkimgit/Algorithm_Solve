import java.util.*;
import java.io.*;

public class BOJ1253 {
    public static void main(String[] args) throws IOException {
        var bf = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bf.readLine());
        var st = new StringTokenizer(bf.readLine());
        long arr[] = new long[N];
        for (int i = 0; i < N; i ++) {
            arr[i] = Long.parseLong(st.nextToken());
        }

        Arrays.sort(arr);
        int result = 0;

        for(int targatPointer = 0; targatPointer < N; targatPointer ++) {
            int startPointer = 0;
            int endPointer = N - 1;
            long target = arr[targatPointer];

            while(startPointer < endPointer) {
                if(arr[startPointer] + arr[endPointer] == target) {
                    if(startPointer != targatPointer && endPointer != targatPointer) {
                        result += 1;
                        break;
                    } else if (startPointer == targatPointer) {
                        startPointer += 1;
                    } else if (endPointer == targatPointer) {
                        endPointer -= 1;
                    }
                } else if (arr[startPointer] + arr[endPointer] < target) {
                    startPointer += 1;
                } else {
                    endPointer -= 1;
                }
            }
        }

        System.out.println(result);
        bf.close();
    }
}
