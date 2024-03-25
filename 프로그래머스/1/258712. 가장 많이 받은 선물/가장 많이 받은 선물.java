import java.util.*;
class Solution {
    public int solution(String[] friends, String[] gifts) {
        int answer = 0;
        int[][] arr = new int[friends.length][friends.length];
        Map<String, Integer> name_map = new HashMap<>();
        // 얘들 이름 map으로 담아서 뽑아 쓰기 
        for(int i = 0; i < friends.length; i++) {
        	name_map.put(friends[i], i);
        }
        // 주고받은 선물 배열 그리기
        for(int i = 0; i < gifts.length; i++) {
        	String[] str_arr= gifts[i].split(" ");
        	arr[name_map.get(str_arr[0])][name_map.get(str_arr[1])] += 1;
        }
        // 접어서 한번에 확인하게 하기(행, 열)
        int [] friends_gift = new int[friends.length];
        for(int i = 0; i < arr.length; i++) {
        	for(int j = 0; j < arr.length; j++) {
        		friends_gift[i] -= arr[j][i];
        	}
        }
        // 각 선물 지수 확인하기 
        for(int i = 0; i < arr.length; i++) {
        	for(int j = 0; j < arr.length; j++) {
        		friends_gift[i] += arr[i][j]; 
        	}
        }
        // 이제 각 값들을 확인하기
        for(int i = 0; i < arr.length; i++) {
        	int next_gift = 0;
        	for(int j = 0; j < arr.length; j++) {
        		if(arr[i][j] > arr[j][i]) {
        			next_gift += 1;
        		}
                else if(arr[i][j] == arr[j][i]){
                    next_gift = friends_gift[i] > friends_gift[j] ? next_gift+1 : next_gift;
                }
                else if(arr[i][j] == 0 && arr[j][i] == 0) {
        			next_gift = friends_gift[i] > friends_gift[j] ? next_gift+1 : next_gift;
        		}
        	}
        	answer = Math.max(answer, next_gift);
        }
        return answer;
    }
}