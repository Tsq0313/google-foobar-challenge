package Company.Google.foobar;

import java.util.ArrayList;
import java.util.List;

public class Doomsday {
    public static int[] solution(int area) {
        int remaining = area;
        List<Integer> results = new ArrayList<>();

        while (remaining > 0){
            int result = (int) Math.sqrt(remaining);
            results.add(result*result);
            remaining -= result*result;
        }
        int[] res = results.stream().mapToInt(Integer::intValue).toArray();
        return res;
    }

    public static void main (String[] args){
        int test = 12;
        for (int solution : solution(test)){
            System.out.print(solution);
        }
    }
}
