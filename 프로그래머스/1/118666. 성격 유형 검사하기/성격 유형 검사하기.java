import java.util.*;
class Solution {
    public String solution(String[] survey, int[] choices) {
    	char[] mbtiArr = new char[] {'R','T','C','F','J','M','A','N'};
        String answer = "";
    	Map<Character, Integer> map = new HashMap<>();
    	for(int i = 0; i < mbtiArr.length; i++) {
    		map.put(mbtiArr[i], 0);
    	}
    	for(int i = 0; i < choices.length; i++) {
    		int score = 4;
    		if(choices[i] > 4) {
    			score = choices[i] - 4;
    			map.put(survey[i].charAt(1), map.get(survey[i].charAt(1))+score);
    		}
    		else if(choices[i] < 4) {
    			score = 4 - choices[i];
    			map.put(survey[i].charAt(0), map.get(survey[i].charAt(0))+score);
    		}
    	}
    	int i = 0;
    	while(i != 8) {
    		if(map.get(mbtiArr[i]) < map.get(mbtiArr[i+1]))
    			answer += mbtiArr[i+1];
    		else
    			answer += mbtiArr[i];
    		i += 2;
    	}
    	
        return answer;
    }
}