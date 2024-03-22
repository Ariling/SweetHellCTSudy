import java.util.*;
class Solution {
    static boolean[][] visited;
	static int[][] copyMaps;
	static int[] dr = {-1,1,0,0};
	static int[] dc = {0,0,-1,1};
	static int r;
	static int c;
    public int solution(int[][] maps) {
    	r = maps.length;
    	c = maps[0].length;
    	copyMaps = maps;
    	visited = new boolean[r][c];
    	visited[0][0] = true;
    	bfs(0,0);
        int answer = 0;
        answer = maps[r-1][c-1] == 1 ? -1 : maps[r-1][c-1];
        return answer;
    }
        public void bfs(int x, int y) {
    	Queue<int []> q = new LinkedList<>();
    	q.add(new int[] {x, y});
    	while(!q.isEmpty()) {
    		int cur[] = q.poll();
    		int curX = cur[0];
    		int curY = cur[1];
    		
    		for(int i = 0; i < 4; i++) {
    			int nextX = curX+dr[i];
    			int nextY = curY+dc[i];
    			if(nextX < 0 || nextY < 0 || nextX >= r || nextY >= c) 
    				continue;
    			if(copyMaps[nextX][nextY] == 0 || visited[nextX][nextY])
    				continue;
    			q.add(new int[] {nextX, nextY});
    			copyMaps[nextX][nextY] = copyMaps[curX][curY] + 1;
    			visited[nextX][nextY] = true;
    		}
    		
    	}
    }
}