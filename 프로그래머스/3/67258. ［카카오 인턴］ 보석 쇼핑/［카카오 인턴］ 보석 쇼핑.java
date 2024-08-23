import java.util.*;
class Solution {
    public int[] solution(String[] gems) {
        // 종류 구하기
        int size = new HashSet<>(Arrays.asList(gems)).size();
        
        int[] answer = new int[2];
        int len = Integer.MAX_VALUE, start = 0;
        
        Map<String, Integer> map = new HashMap<>();
        
        for(int end = 0; end < gems.length; end++){
            map.put(gems[end], map.getOrDefault(gems[end], 0) + 1);
        while (map.get(gems[start]) > 1) {
                map.put(gems[start], map.get(gems[start]) - 1);
                start++;
            }
            if(map.size() == size && len > (end - start)){
                len = end - start;
                answer[0] = start+1;
                answer[1] = end+1;
            }
        }
        return answer;
    }
}