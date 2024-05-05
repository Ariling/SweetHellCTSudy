import java.util.*;
class Solution {
      public int solution(int[] stones, int k) {
            // 이분탐색으로 해야 효율성을 클리어 할 수 있다고 한다...
            // 최소 최대를 이용해 중간값 구하기..
            int min = Integer.MAX_VALUE;
            int max = Integer.MIN_VALUE;
            for (int stone : stones) {
                min = Math.min(min, stone);
                max = Math.max(max, stone);
            }
            while(min < max){
                int mid = (min + max + 1) / 2;
                if(walk(mid, k, stones)){
                    min = mid;
                }else{
                    max = mid - 1;
                }
            }

            return max;
        }
        public boolean walk(int mid, int k, int[] stones){
            int cnt = 0;
            for(int stone : stones){
                if(stone - mid < 0){
                    cnt++;
                }else{
                    cnt = 0;
                }

                if(cnt == k){
                    return false;
                }
            }
            return true;
        }
}