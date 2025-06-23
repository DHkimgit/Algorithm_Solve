import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;


public class BOJ_34017 {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Integer t = Integer.parseInt(br.readLine());

        for (Integer i = 0; i < t; i++) {
            clac(Integer.parseInt(br.readLine()));
        }
    }

    private static void clac(Integer n) {
        if (Math.sqrt(n) % 1 == 0) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }
}