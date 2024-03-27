import java.util.*;
class Solution {
    static Map<String, Integer> map;
	static Map<String, Boolean> check_map;
	static Map<String, Integer> result_map;
    public int[] solution(int[] fees, String[] records) {
        int[] answer = {};
        map = new HashMap<>();
        check_map = new HashMap<>();
        //이걸로 난리쳐보자 그러면 되겠지 시부레 
        result_map = new HashMap<>();
        // records 처리하기
        for(int i = 0; i < records.length; i++) {
        	String[] str_arr = records[i].split(" ");
        	if(str_arr[2].equals("IN")) {
        		int hour_min = Integer.parseInt(str_arr[0].substring(0,2)) * 60 ;
        		int min = Integer.parseInt(str_arr[0].substring(3));
        		map.put(str_arr[1], hour_min+min);
        		//들어온거 확인
        		check_map.put(str_arr[1], true);
        	}
        	else if(str_arr[2].equals("OUT")) {
        		int hour_min = Integer.parseInt(str_arr[0].substring(0,2)) * 60 ;
        		int min = Integer.parseInt(str_arr[0].substring(3));
        		//들어오고 나간 거를 처리해주기
        		map.put(str_arr[1], (hour_min + min)-map.get(str_arr[1]));
        		result_map.put(str_arr[1], result_map.getOrDefault(str_arr[1], 0) + map.get(str_arr[1]));
        		//기존 map의 값은 지워주기(또 들어왔을 때 값을 처리해야되므로)
        		map.remove(str_arr[1]);
        		check_map.put(str_arr[1], false);
        	}
        }
        // 들어오고 나가지 않은 거를 마지막에 처리해주기
        int no_out_time = (60*24) -1;
        for(String key : check_map.keySet()) {
        	if(check_map.get(key) == true) {
        		int time_dif = no_out_time - map.get(key);
        		result_map.put(key, result_map.getOrDefault(key, 0)+time_dif);
        	}
        }
        //answer길이 그냥 냅다 구하기
        List<String> keySet = new ArrayList<>(result_map.keySet());
        answer = new int[keySet.size()];
        Collections.sort(keySet);
        //  차량 번호가 작은 자동차부터 요금을 구하기
        int idx = 0;
        for(String key : keySet) {
        		if(result_map.get(key) <= fees[0]) {
        			answer[idx++] = fees[1];
        		}
        		else
        		{
        			int over_time = result_map.get(key) - fees[0];
        			if(over_time % fees[2] != 0) {
        				int over_fees = fees[3] * ((over_time/fees[2])+1);
        				answer[idx++] = fees[1] + over_fees;
        			}
        			else
        			{
        				int over_fees = fees[3] * ((over_time/fees[2]));
        				answer[idx++] = fees[1] + over_fees;
        			}
        		}
        }
        return answer;
    }
}