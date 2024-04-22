import java.util.*;
class Solution {
	static boolean[] check_arr;
	static int len;
	static Set<Integer> set;
    public int solution(String numbers) {
        int answer = 0;
        check_arr = new boolean[numbers.length()];
        len = numbers.length();
        set = new HashSet<>();
        for(int i = 0; i < len; i++) {
        	check_arr[i] = true;
            dfs(i,0,String.valueOf(numbers.charAt(i)), numbers);
            check_arr[i] = false;
        }
        for(int num : set) {
        	// 소수 찾을 때 이거 쓴대... 나도 잘 몰러..
        	int era_num = (int) Math.sqrt(num);
        	boolean check = true;
        	for(int j = 2; j <= era_num; j++) {
        		// 0 이면 소수가 아니라는 것이므로 PASS
        		if(num % j == 0) {
        			check = false;
        			break;
        		}
        		
        	}
        	if(check == true && num > 1) {
        		answer += 1;
        	}
        }
        return answer;
    }
    public void dfs(int start ,int n, String str, String numbers) {
    	if(n == len) {
    		set.add(Integer.parseInt(str));
    		return;
    	}
    	for(int i = 0; i < len; i++) {
    		if(check_arr[i] == true) {
    			dfs(start,n+1,str, numbers);
    		}else {
    			check_arr[i] = true;
    			dfs(start,n+1, str+String.valueOf(numbers.charAt(i)), numbers);
    			check_arr[i] = false;
    			dfs(start,n+1,str, numbers);
    		}
    	}
    	
    }
}