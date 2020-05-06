import java.io.*;
import java.util.*;
import javafx.util.Pair;

public class aa {
    private static Map<Integer, List<Integer> > al = new HashMap<>();
    private static Map<Integer, Character> characterAt = new HashMap<>();
    private static Map<Integer, Integer> visited = new HashMap<>();
    private static Pair<Character, Integer> bestCharacter = new Pair<>(new Character('z'), -1);

    private static String s;
    private static String t;

    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tt = Integer.parseInt(br.readLine());
        while (tt-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            s = br.readLine();
            t = br.readLine();
            for(int i=0;i<k;i++) {
                st = new StringTokenizer(br.readLine());
                int l = Integer.parseInt(st.nextToken());
                int r = Integer.parseInt(st.nextToken());
                if (!al.containsKey(l)) {
                    al.put(l, new ArrayList<Integer>());
                }
                if (!al.containsKey(r)) {
                    al.put(r, new ArrayList<Integer>());
                }
                al.get(l).add(r);
                al.get(r).add(l);
            }
            for(int i=0;i<n;i++) {
                al.put(100000 + i, new ArrayList<Integer>());
                al.get(100000 + i).add(i);
                if (!al.containsKey(i)) {
                    al.put(i, new ArrayList<Integer>());
                }
                al.get(i).add(100000 + i);
                characterAt.put(i, s.charAt(i));
                characterAt.put(100000 + i, t.charAt(i));
            }
            StringBuilder sb = new StringBuilder();
            for(int i=0;i<n;i++) {
                sb.append(optimumCharacter(100000 + i));
            }
            System.out.println(sb.toString());
        }
    }

    private static int getIndex(int i) {
        if (i >= 100000) {
            return i - 100000;
        }
        return i;
    }

    private static Character optimumCharacter(int pos) {
        visited = new HashMap<>();
        bestCharacter = new Pair<>(characterAt.get(pos), pos);
        traverseGraph(pos, pos);
        if (bestCharacter.getValue() != pos) {
            Character old = characterAt.get(pos);
            characterAt.put(pos, bestCharacter.getKey());
            characterAt.put(bestCharacter.getValue(), old);
        }
        return characterAt.get(pos);
    }

    private static void traverseGraph(int curPos, int startingPos) {
        if (visited.containsKey(curPos)) {
            return;
        }
        visited.put(curPos, 1);
        for (int item : al.get(curPos)) {
            if (visited.containsKey(item)) {
                continue;
            }
            if (characterAt.get(item) < bestCharacter.getKey()
                    && ((item >= 100000 && getIndex(item) > getIndex(startingPos))
                        || item < 100000
                        )) {
                            bestCharacter = new Pair<>(characterAt.get(item), item);
            }
            traverseGraph(item, startingPos);
        }
    }
}