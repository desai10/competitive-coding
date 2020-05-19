import java.io.*;
import java.util.*;

public class BinaryPeriod {
    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tt = Integer.parseInt(br.readLine());
        while (tt-- > 0) {
            String t = br.readLine();
            StringBuilder sb = new StringBuilder();
            char[] ca = t.toCharArray();
            Arrays.sort(ca);
            if (ca[0] == ca[t.length() - 1]) {
                System.out.println(t);
            } else {
                char pre = t.charAt(0);
                sb.append(pre);
                int i = 0;
                while (i < t.length()) {
                    if (pre == t.charAt(i)) {
                        pre = pre == '0' ? '1' : '0';
                    } else {
                        pre = t.charAt(i);
                        i++;
                    }
                    sb.append(pre);
                }
                System.out.println(sb.toString());
            }
        }
    }
}