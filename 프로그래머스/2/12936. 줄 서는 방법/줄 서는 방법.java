import java.util.*;
class Solution {
    public int[] solution(int n, long k) {
        int[] answer = new int[n];
        List<Integer> list = new ArrayList<>();
        // n만큼 list 초기화하기
        long f = 1;
        for(int i=1; i<=n; i++) {
            list.add(i);
            f *= i;
        }
        // k - 1번째를 구해야함. -> 배열이기 때문
        k--; 
        int idx = 0;
        while(idx < n) {
            f /= n - idx;
            answer[idx++] = list.remove((int) (k / f));
            k %= f;
        }

        return answer;
    }
}