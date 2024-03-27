import java.util.*;
class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        String [] num_str = new String[numbers.length];
        for(int i = 0; i < num_str.length; i++) {
        	num_str[i] = String.valueOf(numbers[i]);
        }
        Arrays.sort(num_str, new Comparator<String>() {
        	public int compare(String x, String y) {
        		return (y+x).compareTo(x+y);
        	}
        });
        //아니 이거를 생각해내라고..? 다 0일경우...
        if(num_str[0].equals("0")){
            return "0";
        }
        for(int i = 0; i < num_str.length; i++) {
        	answer += num_str[i];
        }
        return answer;
    }
}