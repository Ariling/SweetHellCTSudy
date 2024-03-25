import java.util.*;
class Solution {
    public int solution(int[] queue1, int[] queue2) {
    	long mid = 0;
    	long q1_sum = 0;
    	long q2_sum = 0;
    	int answer = 0;
    	Queue<Integer> q1 = new LinkedList<>();
    	Queue<Integer> q2 = new LinkedList<>();
    	for(int i = 0; i < queue1.length; i++) {
    		mid += queue1[i];
    		q1_sum += queue1[i];
    		mid += queue2[i];
    		q2_sum += queue2[i];
    	}
    	if(mid % 2 == 1) return -1;
    	mid /= 2;
        for(int i = 0; i < queue1.length; i++) {
    		q1.add(queue1[i]);
    		q2.add(queue2[i]);
    	}
    	while(q1_sum != mid && q2_sum != mid) {
    		if(q1_sum > mid) {
    			int num = q1.poll();
    			q1_sum -= num;
    			q2_sum += num;
    			q2.add(num);
    			answer += 1;
    		}
    		if(q2_sum > mid) {
    			int num = q2.poll();
    			q1_sum += num;
    			q2_sum -= num;
    			q1.add(num);
    			answer+= 1;
    		}
            if(answer == queue1.length * 4)
                return -1;
    	}
    	return answer;
    }

}