import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ2805 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        Integer N = Integer.parseInt(st.nextToken());
        Integer M = Integer.parseInt(st.nextToken());

        StringTokenizer st2 = new StringTokenizer(bf.readLine());
        int[] heights = new int[N];

        int index = 0;
        int right = 0;

        while(st2.hasMoreTokens()) {
            int k = Integer.parseInt(st2.nextToken());
            heights[index++] = k;
            if(k >= right) right = k;
        }

        int left = 0;
        int result = 0;

        while(left <= right) {
            int mid = (left + right) / 2;
            if(decision(heights, mid, M)) {
                result = mid;
                left = mid + 1;
            }
            else{
                right = mid - 1;
            }
        }
        System.out.println(result);
    }
    public static boolean decision(int[] targets, Integer param, Integer target) {
        long cut = 0;
        for(int height : targets) {
            cut += Math.max(0, height - param);
            if (cut >= target) return true;
        }
        return cut >= target;
    }
}
