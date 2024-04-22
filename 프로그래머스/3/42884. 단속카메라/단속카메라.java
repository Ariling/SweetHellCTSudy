import java.util.*;
class Solution {
    public int solution(int[][] routes) {
        int answer = 0;
        Arrays.sort(routes, new Comparator<int[]>(){
            @Override
            public int compare(int[] a, int[] b){
                return a[1] != b[1] ? a[1] - b[1] : a[0] - b[0];
            }
        });
        int cam_pos = Integer.MIN_VALUE;
        for(int[] info : routes){
            if(info[0] > cam_pos){
                cam_pos = info[1];
                answer += 1;
            }
        }
        return answer;
    }
}