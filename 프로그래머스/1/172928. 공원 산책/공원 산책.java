class Solution {
    public int[] solution(String[] park, String[] routes) {
    	char[][] arr = new char[park.length][park[0].length()];
    	for(int i = 0; i < park.length; i++) {
    		arr[i] = park[i].toCharArray();
    	}
    	int r = 0; int c = 0;
    	out : for(int i = 0; i < park.length; i++) {
    		for(int j = 0; j < park[0].length(); j++) {
    			if(arr[i][j] == 'S') {
    				r = i; c = j;
    				break out;
    			}
    		}
    	}
    	for(int i = 0; i < routes.length; i++) {
    		String[] str_arr = routes[i].split(" ");
    		int move = Integer.parseInt(str_arr[1]);
    		switch(str_arr[0]) {
    		case "E":
    			if(c + move >= park[0].length() || park[r].substring(c,c+move+1).contains("X"))
    				break;
    			c += move;
    			break;
    		case "W":
    			if(c - move < 0 || park[r].substring(c-move,c).contains("X"))
    				break;
    			c -= move;
    			break;
    		case "N" :
    			if(r - move < 0 || checkBarrier(r,c,arr,str_arr[0],move) == false)
    				break;
    			r -= move;
    			break;
    		case "S":
    			if(r + move >= park.length || checkBarrier(r,c,arr,str_arr[0],move) == false)
    				break;
    			r += move;
    			break;
    		}
    	}
        int[] answer = {};
        answer = new int[]{r,c};
        return answer;
    }
    public boolean checkBarrier (int r, int c, char[][] arr, String case_str, int move) {
    	if(case_str.equals("N")) {
    		for(int i =r-move; i <= r; i++ ) {
    			if (arr[i][c] == 'X') return false;
    		}
    		return true;
    	}else {
    		for(int i =r+move; i >= r; i-- ) {
    			if (arr[i][c] == 'X') return false;
    		}
    		return true;
    	}
    }
}