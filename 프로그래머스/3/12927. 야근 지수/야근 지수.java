import java.util.*;
// 야근지수
class Solution {
    public long solution(int n, int[] works) {
        // 야근을 하면 피로도가 쌓인다.
        // Nㅅ간 동안 야근 피로도를 최소화하도록 일하기
        // 1시간 동안 1만큼을 처리
        // 퇴근까지 남은 N시간과 각 일에 대한 작업량 works에 대해
        // 야근 피로도를 최소화한 값
        // 아아 n은 각 시간을 나타낸 거고 거기서 줄이는 작업을 하는 거구나?
        // 1. 큰 것부터 하나씩 줄여나간다. 다만 다 0이면 result도 0이다.
        // 2. 근데 이거를 하나하나 다 비교하면서 줄이면 분명 시간초과가 뜰거란 말여?
        // 아! 해시쓸까? 그러면 문제가 없을 것 같은디
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for(int i = 0; i < works.length; i++)
        	pq.offer(works[i]);
        for(int i = 1; i <= n; i++) {
        	if(pq.isEmpty())
        		break;
        	int num = pq.poll() - 1;
        	if(num != 0)
        		pq.offer(num);
        }
        if(pq.isEmpty())
        	return 0;
        else {
            long answer = 0;
            while(!pq.isEmpty()) {
            	answer += Math.pow(pq.poll(), 2);
            }
            return answer;
        }
    }
}