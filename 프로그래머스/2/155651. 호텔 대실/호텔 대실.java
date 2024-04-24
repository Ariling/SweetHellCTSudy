import java.util.*;
class Solution {
    public int solution(String[][] book_time) {
        int answer = 0;
        int[][] change_time = new int[book_time.length][book_time[0].length];
        for(int i = 0; i < book_time.length; i++) {
        	for(int j = 0; j < book_time[0].length; j++) {
        		String[] time_arr = book_time[i][j].split(":");
        		int hour = Integer.parseInt(time_arr[0]) * 60;
        		int min = Integer.parseInt(time_arr[1]);
        		int time = hour+min;
        		change_time[i][j] = time;
        	}
        }
        Arrays.sort(change_time, new Comparator<int[]>() {
        	@Override
        	public int compare(int[] a, int[] b) {
        		return a[0]!=b[0] ?  a[0] - b[0] : a[1] - b[1];
        	}
        });
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int i = 0; i < change_time.length; i++) {
        	if(!pq.isEmpty() && change_time[i][0] >= pq.peek()+10) {
        		pq.poll();
        	}
        	//종료 시간을 담아야 한다. 그래야 시작시간과 비교해서 넣을 수 있기 때문
        	pq.offer(change_time[i][1]);
        }
        answer = pq.size();
        return answer;
    }
}