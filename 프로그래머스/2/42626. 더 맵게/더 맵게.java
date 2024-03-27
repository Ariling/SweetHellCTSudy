import java.util.*;
class Solution {
    static PriorityQueue<Integer> pq;
    public int solution(int[] scoville, int K) {
    	pq = new PriorityQueue<>();
    	int answer = 0;
        Arrays.sort(scoville);
    	for(int i = 0; i < scoville.length; i++) {
    		pq.add(scoville[i]);
    	}
    	
    	while(pq.peek() < K) {
    		int a = pq.poll(); 
    		int b = pq.poll() * 2;
    		int c = a + b;
    		pq.add(c);
    		answer += 1;
            if(pq.size() == 1 && pq.peek() < K){
                answer = -1;
                return answer;
            }
    	}
    	
        return answer;
    }
}