import java.util.*;
class Solution {
    public int[] solution(String[] operations) {
        int[] answer = {};
        Map<Integer, Integer> map = new HashMap<>();
        //내림차순을 위한 sort method사용하기
        PriorityQueue<Integer> max_q = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> min_q = new PriorityQueue<>();
        // 명령어에 따른 로직 처리
        for(int i = 0; i < operations.length; i++) {
        	String[] str_arr= operations[i].split(" ");
        	if(str_arr[0].equals("I")) {
        		int key = Integer.parseInt(str_arr[1]);
        		map.put(key, map.getOrDefault(map.get(key), 0)+1);
        		max_q.offer(key);
        		min_q.offer(key);
        	}
        	else {
        		// 최대를 뺄 경우
        		if(str_arr[1].equals("1")) {
        			// 안 비어있고, 해당 peek의 값이 0일때는 자동으로 뺴줘야한다. map의 개수랑 동일시 하기
					while(!max_q.isEmpty() && map.get(max_q.peek()) == 0) {
						max_q.poll();
					}
					if(!max_q.isEmpty()) {
	        			int key = max_q.poll();
	        			map.put(key, map.get(key) - 1);
					}
        		}else {
        			while(!min_q.isEmpty() && map.get(min_q.peek()) == 0) {
        				min_q.poll();
        			}
        			if(!min_q.isEmpty()) {
            			int key = min_q.poll();
            			map.put(key, map.get(key) - 1);
        			}
        		}
        	}
        }
        //마지막으로 다시 한 번 하기 ! 
		while(!max_q.isEmpty() && map.get(max_q.peek()) == 0) {
			max_q.poll();
		}
		while(!min_q.isEmpty() && map.get(min_q.peek()) == 0) {
			min_q.poll();
		}
		int max = max_q.isEmpty() ? 0 : max_q.peek();
		int min = min_q.isEmpty() ? 0 : min_q.peek();
		answer = new int[] {max, min};
        return answer;
    }
}