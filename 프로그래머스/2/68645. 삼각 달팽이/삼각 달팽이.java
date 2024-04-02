import java.util.*;
class Solution {
	static int[][] arr;
	static List<Integer> list;
	static int snail_maxNum;
	static int dir;
    public int[] solution(int n) {
        int[] answer = {};
        arr = new int[n][n];
        list = new ArrayList<>();
        snail_maxNum = (n*(n+1))/2;
        int row_u = 0, column_l = 0;
        int column_r = n-1;
        int row_d = n - 1;
        //아래 옆 대각선 방향
        dir = 0;
        int idx = 0;
        while(idx < snail_maxNum) {
        	// 아래 방향
        	for(int i = row_u; i <= row_d && idx < snail_maxNum; i++)
        		arr[i][column_l] = ++idx;
        	column_l++;
        	// 오른쪽 방향
        	for(int i = column_l; i <= column_r && idx < snail_maxNum; i++) {
        		if(arr[row_d][i] != 0)
        			break;
        		arr[row_d][i] = ++idx;
        	}
        	row_d--;
        	column_r--;
        	// 대각선 방향 주의하기!
        	for(int i = 0; i <= row_d && idx < snail_maxNum; i++) {
        		if(arr[row_d-i][column_r-i] != 0) 
        			break;
        		arr[row_d-i][column_r-i] = ++idx;
        	}
        	row_u += 2;
        	column_r --;
        	}
        for(int i = 0; i < arr.length; i++) {
        	for(int j = 0; j < arr.length; j++) {
        		if(arr[i][j] != 0)
        			list.add(arr[i][j]);
        	}
        }
        answer = new int[list.size()];
        for (int i = 0 ; i < list.size() ; i++) 
            answer[i] = list.get(i);
        
        return answer;
    }
}