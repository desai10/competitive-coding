import java.io.*;

class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int ii = 1;ii <= t;ii++) {
            String i = br.readLine();
            String p = br.readLine();
            
            int ct = 0;
            int ci = 0;
            int cp = 0;
            
            while (ci < i.length() && cp < p.length()) {
                if (i.charAt(ci) == p.charAt(cp)) {
                    ci += 1;
                    cp += 1;
                } else {
                    cp += 1;
                    ct += 1;
                }
            }
            
            while (cp < p.length()) {
                cp += 1;
                ct += 1;
            }
            
            if (ci == i.length()) {
                System.out.println("Case #" + ii + ": " + ct);
            } else {
                System.out.println("Case #" + ii + ": IMPOSSIBLE");
            }
        }
    }
}