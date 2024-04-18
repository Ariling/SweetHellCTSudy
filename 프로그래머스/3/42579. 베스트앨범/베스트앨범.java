import java.util.*;

class Solution {
	static List<int[]> list;
	static Map<String, Integer> map;
    public int[] solution(String[] genres, int[] plays) {
        int[] answer = {};
    	// 장르별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범 출시
    	// 노래는 고유 번호로 구분
    	map = new HashMap<>();
    	for(int i = 0; i < plays.length; i++)
    		map.put(genres[i], map.getOrDefault(genres[i], 0)+plays[i]);
    	List<String> keySet = new ArrayList<>(map.keySet());
    	// key값가지고 value값을 기준으로 정렬하는 방법..(이거를 어떻게 외우냐고)
    	keySet.sort((o1,o2) -> map.get(o2).compareTo(map.get(o1)));
    	List<Integer> result_list = new ArrayList<>();
    	for(int i = 0; i < keySet.size(); i++) {
    		list = new ArrayList<>();
    		for(int j = 0; j < plays.length; j++) {
    			if(keySet.get(i).equals(genres[j])) {
    				list.add(new int[] {plays[j], j});
    			}
    		}
    		// int[] list 정렬하는 방법 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 환장하겠다
        	Collections.sort(list, new Comparator<int []>() {
        		@Override
        		public int compare(int[] a, int[] b) {
        			return a[0] != b[0] ? b[0] - a[0] : a[1] - b[1];
        		}
        	});
        	for(int j = 0; j < list.size(); j++) {
        		if(j >= 2)
        			break;
        		result_list.add(list.get(j)[1]);
        	}
    	}
    	int [] result = new int[result_list.size()];
    	for(int i = 0; i < result_list.size(); i++) {
    		result[i] = result_list.get(i);
    	}
    	answer = result;
        return answer;
    }
}