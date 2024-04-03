import java.util.*;
class Solution {
	static int[] p;
	static int differ;
	//끝 부분의 갯수를 알기 위한 방법
	static Map<Integer, Integer> map;
    public int solution(int n, int[][] wires) {
        int answer = -1;
        //최소를 구하는 것이므로
        differ = Integer.MAX_VALUE;
        p = new int[n+1];
        for(int i = 0; i < wires.length; i++) {
        	map = new HashMap<>();
            for(int j = 1; j < n+1; j++)
            	p[j] = j;
            // union 시키기 
            for(int j = 0; j < wires.length; j++) {
            	if(i == j)
            		continue;
            	int x = wires[j][0];
            	int y = wires[j][1];
            	if(findset(y) != findset(x))
            		p[findset(x)] = findset(y);
            }
            // 잠만 findset(j)와 findset(findset(j))가 같네..? 
            List<Integer> list = new ArrayList<>();
            for(int j = 1; j < n+1; j++) {
            	if(p[j] == j)
            		list.add(j);
            	map.put(findset(j), map.getOrDefault(findset(j), 0)+1);
            }
            //list가 2개라는 거는 2개로 잘 나뉘어졌다는 뜻
        	if(list.size() == 2) 
        		differ = Math.min(differ, Math.abs(map.get(list.get(0))-map.get(list.get(1))));
        		
        }
        answer = differ;
        return answer;
    }
    public int findset(int x) {
    	if(x != p[x])
    		p[x] = findset(p[x]);
    	return p[x];
    }
}