import java.util.*;
class Solution {
	static List<int[]> list;
    public int[][] solution(int n) {
        int[][] answer = {};
        list = new ArrayList<>();
        hanoi(n,1,3,2);
        answer = new int[list.size()][2];
        for(int i = 0; i < list.size(); i++) {
        	answer[i] = list.get(i);
        }
        return answer;
    }
    public void hanoi(int n, int from, int to, int other) {
    	// n이 0이 되면 끝낸다
    	if(n == 0)
    		return;
    	// n-1층만큼 2번으로 옮겨야하므로 재귀로 옮겨둔다.
    	hanoi(n-1,from,other,to);
    	// 이거는 맨 밑층의 이동경로를 담는 리스트
    	list.add(new int[] {from, to});
    	// n-1층만큼을 to로 가게 재귀를 돌린다. 
    	hanoi(n-1,other,to,from);
    }
}