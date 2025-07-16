import java.util.*;
import java.io.*;

public class BOJ12891 {
    public static void main(String[] args) throws IOException{
        var bf = new BufferedReader(new InputStreamReader(System.in));
        var st = new StringTokenizer(bf.readLine());
        int S = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());
        char[] array = bf.readLine().toCharArray();
        int startPointer = 0;
        int endPointer = P - 1;
        int[] dnaIndex = new int[4];
        for (int i = 0; i <= endPointer; i ++) {
            switch (array[i]) {
                case 'A':
                    dnaIndex[0] += 1;
                    break;
                case 'C':
                    dnaIndex[1] += 1;
                    break;
                case 'G':
                    dnaIndex[2] += 1;
                    break;
                case 'T':
                    dnaIndex[3] += 1;
                    break;
                default:
                    break;
            }
        }

        st = new StringTokenizer(bf.readLine());
        int minA = Integer.parseInt(st.nextToken());
        int minC = Integer.parseInt(st.nextToken());
        int minG = Integer.parseInt(st.nextToken());
        int minT = Integer.parseInt(st.nextToken());
        int result = 0;

        while (endPointer != S) {
            if(dnaIndex[0] >= minA && dnaIndex[1] >= minC && dnaIndex[2] >= minG && dnaIndex[3] >= minT) {
                result += 1;
            }
            switch (array[startPointer]) {
                case 'A':
                    dnaIndex[0] -= 1;
                    break;
                case 'C':
                    dnaIndex[1] -= 1;
                    break;
                case 'G':
                    dnaIndex[2] -= 1;
                    break;
                case 'T':
                    dnaIndex[3] -= 1;
                    break;
                default:
                    break;
            }
            startPointer += 1;
            endPointer += 1;
            if(endPointer == S) break;
            switch (array[endPointer]) {
                case 'A':
                    dnaIndex[0] += 1;
                    break;
                case 'C':
                    dnaIndex[1] += 1;
                    break;
                case 'G':
                    dnaIndex[2] += 1;
                    break;
                case 'T':
                    dnaIndex[3] += 1;
                    break;
                default:
                    break;
            }
        }

        System.out.println(result);
    }
}
