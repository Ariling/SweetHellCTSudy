import java.util.*;
class Solution {
    static Map<String, String> id_map;
	static Queue<String> chat_queue;
    public String[] solution(String[] record) {
    	id_map = new HashMap<>();
    	chat_queue = new LinkedList<>();
        String[] answer = {};
        List<String> answer_list = new ArrayList<>();
        for(int i = 0; i < record.length; i++) {
        	String[] str_arr = record[i].split(" ");
        	//Leave는 최대 Index가 1이다.
        	if(str_arr[0].equals("Leave")) {
        		chat_queue.add(str_arr[0]+" "+str_arr[1]);
        	}else {
            	id_map.put(str_arr[1], str_arr[2]);
            	// Change냐 Enter냐만 구분하여 넣어놓기
            	if(str_arr[0].equals("Change"))
            		continue;
            	else
            		chat_queue.add(str_arr[0]+" "+str_arr[1]);
        	}
        }
        while(!chat_queue.isEmpty()) {
        	String answer_str = chat_queue.poll();
        	String[] str_arr = answer_str.split(" ");
        	if(str_arr[0].equals("Enter")) {
        		answer_list.add(id_map.get(str_arr[1])+"님이 들어왔습니다.");
        	}else {
        		answer_list.add(id_map.get(str_arr[1])+"님이 나갔습니다.");
        	}
        }
        answer = answer_list.toArray(answer);
        return answer;
    }
}