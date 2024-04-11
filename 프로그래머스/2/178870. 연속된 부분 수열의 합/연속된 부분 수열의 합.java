class Solution {
	static int min_start;
	static int min_length;
	static int[] min_length_arr;
    public int[] solution(int[] sequence, int k) {
        int[] answer = {};
        min_length = Integer.MAX_VALUE;
        min_length_arr = new int[2];
        int start = 0;int end = 0; int sum = 0;
        // 투 포인터 종료 부분 잘 알아두기... 이렇게 종료하는게 맘이 편하다..
        while(start < sequence.length) {
        	if(sum > k || end == sequence.length) 
        		sum -= sequence[start++];
        	else {
        		if(end < sequence.length)
            		sum += sequence[end++];
        	}
        	if(sum == k) {
        		int dif = end - start;
                if(dif < min_length){
                    min_length = dif;
                    min_length_arr[0] = start;
                    min_length_arr[1] = end - 1;
                }else if(dif == min_length){
                    if(start < min_length_arr[0]){
                        min_length_arr[0] = start;
                        min_length_arr[1] = end - 1;
                    }
                }
                sum -= sequence[start++];
        	}
        }
        answer = min_length_arr;
        return answer;
    }
}