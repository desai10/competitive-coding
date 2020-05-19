import java.io.*;
import java.util.*;

public class RoadToZero {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while(t-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            long x = Long.parseLong(st.nextToken());
            long y = Long.parseLong(st.nextToken());
            st = new StringTokenizer(br.readLine());
            long a = Long.parseLong(st.nextToken());
            long b = Long.parseLong(st.nextToken());
            long tot = 0;
            if (2 * a <= b) {
                tot = Math.abs(x) * a;
                tot += Math.abs(y) * a;
            } else {
                if ((x >= 0 && y >= 0) || (x <= 0 && y <= 0)) {
                    tot += (Math.min(Math.abs(x), Math.abs(y))) * b;
                    tot += (Math.abs(x) - Math.min(Math.abs(x), Math.abs(y))) * a;
                    tot += (Math.abs(y) - Math.min(Math.abs(x), Math.abs(y))) * a;
                } else {
                    tot = Math.abs(x) * a;
                    tot += Math.abs(y) * a;
                }
            }
            System.out.println(tot);
        }
    }
}