import java.io.*;
import java.util.StringTokenizer;

public class BOJ_34028 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        Integer year = Integer.parseInt(st.nextToken());
        Integer month = Integer.parseInt(st.nextToken());
        Integer day = Integer.parseInt(st.nextToken());

        Integer yearResult = year - 2015;
        
        Integer monthResult;

        if (month == 12) {
            monthResult = 5;
        } else if (month <= 2) {
            monthResult = 1;
        } else if (month >= 3 && month <= 5) {
            monthResult = 2;
        } else if (month >= 6 && month <= 8) {
            monthResult = 3;
        } else {
            monthResult = 4;
        }

        Integer result = yearResult * 4 + monthResult;
        System.out.println(result);
    }
}
