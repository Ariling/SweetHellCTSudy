import java.util.*;
class Solution {
    static Queue<Integer> q = new LinkedList<>();
    static int[] dis_arr;
    static boolean[] visited;
    static ArrayList<Integer>[] list;
    public int solution(int n, int[][] edge) {
        int answer = 0;
        // 거리를 구해야 하기 때문
        dis_arr = new int[n+1];
        visited = new boolean[n+1];
        list = new ArrayList[n+1];
        // 이렇게 초기화가 가능하대... 몰랐음..
        for(int i = 0; i < n+1; i++){
            list[i] = new ArrayList<>();
        }

        for(int i = 0; i < edge.length; i++){
            int a = edge[i][0];
            int b = edge[i][1];
            list[a].add(b);
            list[b].add(a);
        }

        q.add(1);
        visited[1] = true;
        while(!q.isEmpty()){
            int a = q.poll();
            for(int b : list[a]){
                if(visited[b])
                    continue;
                else{
                    q.add(b);
                    dis_arr[b] = dis_arr[a]+1;
                    visited[b] = true;
                }
            }
        }
        Arrays.sort(dis_arr);
        for(int i = dis_arr.length - 1; i >= 0; i--){
            if(dis_arr[i] == dis_arr[dis_arr.length -1])
                answer++;
            if(dis_arr[i] < dis_arr[dis_arr.length -1])
                break;
        }
        return answer;
}
}