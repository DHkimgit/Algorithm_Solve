import java.util.*;
import java.io.*;

public class BOJ11003 {
    public static void main(String[] args) throws IOException {
        var bf = new BufferedReader(new InputStreamReader(System.in));
        var st = new StringTokenizer(bf.readLine());
        var sb = new StringBuilder();
        int N = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(bf.readLine());
        Deque<Node> deque = new LinkedList<>();

        for(int i = 0; i < N; i++) {
            int currentValue = Integer.parseInt(st.nextToken());
            while(!deque.isEmpty() && deque.getLast().value > currentValue) {
                deque.removeLast();
            }
            deque.addLast(new Node(currentValue, i));

            if (deque.getFirst().index <= i - L) {
                deque.removeFirst();
            }
            sb.append(deque.getFirst().value).append(" ");
        }
        bf.close();
        System.out.println(sb);
    }

    public static class Node {
        public int value;
        public int index;

        Node(int value, int index) {
            this.value = value;
            this.index = index;
        }
    }
}
