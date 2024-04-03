import java.util.*;
class Solution {
	static Map<String, Integer> map;
	static List<String> result_list;
	static char[] combi_arr;
	static boolean[] check;
	static int len;
	static int N;
    public String[] solution(String[] orders, int[] course) {
        String[] answer = {};
        result_list = new ArrayList<>();
        for(int i = 0; i < course.length; i++) {
        	// 갯수 뽑기
        	N = course[i];
        	map = new HashMap<>();
            for(int j = 0; j < orders.length; j++) {
            	if(orders[j].length() < N) continue;
            	else {
                	combi_arr = orders[j].toCharArray();
                	Arrays.sort(combi_arr);
                	check = new boolean[combi_arr.length];
                	combination(0,0);
            	}
            }
            List<String> keySet = new ArrayList<>(map.keySet());
            if(keySet.size() == 0) 
            	continue;
            else {
                keySet.sort((o1, o2) -> map.get(o2).compareTo(map.get(o1)));
                // 이거랑 같은 값만 리스트에 추가하겠다.
                int T = map.get(keySet.get(0));
                if(T < 2) continue;
                else {
                	result_list.add(keySet.get(0));
                    for(int j = 1; j < keySet.size(); j++) {
                    	if(map.get(keySet.get(j)) < T)
                    		break;
                    	else
                    		result_list.add(keySet.get(j));
                    }
                }
            }
        }
        Collections.sort(result_list);
        answer = new String[result_list.size()];
        for(int i = 0; i < answer.length; i++)
        	answer[i] = result_list.get(i);
        return answer;
    }
    public void combination(int r, int c) {
    	if(r == N) {
    		String str = "";
    		for(int i = 0; i < check.length; i++) {
    			if(check[i] == true)
    				str = str + String.valueOf(combi_arr[i]);
    		}
    		map.put(str, map.getOrDefault(str, 0)+1);
    		return;
    	}
        if(c == combi_arr.length)
        	return;
        check[c] = true;
        combination(r+1, c+1);
        check[c] = false;
        combination(r, c+1);
    }
}