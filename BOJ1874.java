import java.io.*;
import java.util.Stack;

public class BOJ1874 {
    public static void main(String[] args) throws IOException {
        var bf = new BufferedReader(new InputStreamReader(System.in));
        var sb = new StringBuilder();
        int n = Integer.parseInt(bf.readLine());
        Stack<Integer> stack = new Stack<>();
        int num = 1;
        boolean flag = true;

        for(int i = 0; i < n; i++) {
            int val = Integer.parseInt(bf.readLine());
            if(val >= num) {
                while (val >= num) {
                    stack.push(num);
                    num += 1;
                    sb.append("+").append('\n');
                }
                stack.pop();
                sb.append("-").append('\n');
            } else {
                int top = stack.pop();
                if (top > val) {
                    System.out.println("NO");
                    flag = false;
                    break;
                } else {
                    sb.append("-").append('\n');
                }
            }
        }

        if(flag) System.out.println(sb);
    }
}
