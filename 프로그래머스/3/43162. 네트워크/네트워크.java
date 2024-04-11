class Solution {
    static boolean[] checked;
    static int[][] copy_arr;
    static int search_length;
    public int solution(int n, int[][] computers) {
        int answer = 0;
        checked = new boolean[computers.length];
        search_length = computers.length;
        copy_arr = computers.clone();
        for(int i = 0; i < computers.length; i++){
            boolean flag = true;
            for(int j = 0; j < checked.length; j++){
                if(checked[j] == false){
                    flag = false;
                    break;
                }
            }
            if(flag == true) break;
            if(checked[i] == true) continue;
            else{
                answer++;
                dfs(i);
            }
        }
        return answer;
    }
    public void dfs(int n){
        if(n == search_length)
            return;
        checked[n] = true;
        for(int i = 0; i < copy_arr.length; i++){
            if(copy_arr[n][i] == 1 && checked[i] == false){
                checked[i] = true;
                dfs(i);
            }
        }
    }
}