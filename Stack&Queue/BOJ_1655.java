import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;

public class BOJ1655 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());
        MiddleQueue queue = new MiddleQueue();
        for(int i = 0; i < n; i++) {
            Integer inserted = Integer.parseInt(bf.readLine());
            System.out.println(queue.insert(inserted));
        }
    }
}
class MiddleQueue {
    private PriorityQueue<Integer> leftQueue = new PriorityQueue<>(Collections.reverseOrder());
    private PriorityQueue<Integer> rightQueue = new PriorityQueue<>();

    public Integer insert(Integer n) {
        if(leftQueue.isEmpty()) {
            leftQueue.add(n);
            return n;
        }
        Integer leftValue = leftQueue.peek();

        if(n > leftValue) {
            rightQueue.add(n);
        } else{
            leftQueue.add(n);
        }

        if(leftQueue.size() - rightQueue.size() >= 2) {
            rightQueue.add(leftQueue.poll());
        } else if (rightQueue.size() - leftQueue.size() >= 1) {
            leftQueue.add(rightQueue.poll());
        }

        return leftQueue.peek();
    }
}
