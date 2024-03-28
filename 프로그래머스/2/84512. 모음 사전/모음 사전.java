import java.util.*;
class Solution {
	static List<String> list;
	static int cnt;
	static String copy_str;
	static String[] str_arr = {"A","E","I","O","U"};
    public int solution(String word) {
        int answer = 0;
        // 그냥 리스트를 활용하면 되었구나... 근데 리스트 말고는 안되는지? 
        list = new ArrayList<>();
        dfs("",0);
        int size = list.size();
        for(int i = 0; i < size; i++) {
        	if(list.get(i).equals(word)) {
        		answer = i;
        		break;
        	}
        }
        return answer;
    }
    public void dfs(String str,int length) {
    	list.add(str);
    	if (length == 5) return;
    	for(int i = 0; i < 5; i++) {
    		dfs(str+str_arr[i], length+1);
    	}
    }
}