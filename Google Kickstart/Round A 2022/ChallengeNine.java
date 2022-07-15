import java.io.*;

class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        
        for (int i = 1;i <= t;i++) {
            String s = br.readLine();
            long sm = 0;
            for (int j = 0;j < s.length();j++) {
                sm += Character.getNumericValue(s.charAt(j));
            }
            long req = sm % 9;
            if (req != 0) {
                req = 9 - req;
            }
            
            StringBuilder sb = new StringBuilder(s);
            boolean done = false;
            
            int st = 0;
            if (req == 0) {
                st = 1;
            }
            
            for (int j = st;j < s.length();j++) {
                if (req < Character.getNumericValue(s.charAt(j))) {
                    sb.insert(j, String.valueOf(req).toCharArray(), 0, 1);
                    done = true;
                    break;
                }
            }
            
            if (!done) {
                sb.append(req);
            }
            
            System.out.println("Case #" + i + ": " + sb.toString());
        }
    }
}