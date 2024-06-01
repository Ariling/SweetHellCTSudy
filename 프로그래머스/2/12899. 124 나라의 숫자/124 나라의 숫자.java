class Solution {
	public static String solution(int n) {
		String answer = "";
		String[] nums = {"4", "1", "2"};
		
		while(n>0) {
			answer = nums[n%3] + answer;
			n = (n-1)/3;
		}
		return answer;
	}
}