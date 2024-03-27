import java.util.*;
class Solution {
    public int[] solution(int[] prices) {
        int[] answer = {};
        answer = new int[prices.length];
        Stack<Integer> stack = new Stack<>();
        Stack<Integer> idx_stack = new Stack<>();
        stack.push(prices[0]);
        idx_stack.push(0);
        for(int i = 1; i < prices.length; i++) {
        	if(!stack.isEmpty()) {
                while(!stack.isEmpty() && stack.peek() > prices[i])
                {
                    answer[idx_stack.peek()] = i-idx_stack.peek();
        		    stack.pop();
        		    idx_stack.pop();
                }
        	}
            stack.push(prices[i]);
        	idx_stack.push(i);
        }
        while(!stack.isEmpty()) {
        	answer[idx_stack.peek()] = answer.length - idx_stack.peek() - 1;
        	stack.pop();
        	idx_stack.pop();
        }
        return answer;
    }
}