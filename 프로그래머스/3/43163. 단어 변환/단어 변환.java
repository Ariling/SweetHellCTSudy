class Solution {
    static int min_cnt;
    static boolean[] checked;
    static String[] share_words;
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        boolean exist = true;
        for(int i = 0; i < words.length; i++){
            if(target.equals(words[i])) {
                exist = true;
            	break;
            }
            exist = false;
        }
        if(exist == false)
            return 0;
        // 이거를 잘 알아두기! 
        min_cnt = Integer.MAX_VALUE;
        checked = new boolean[words.length];
        share_words = words.clone();
        dfs(begin, target , 0);
        answer = min_cnt;
        return answer;
    }
    public void dfs(String begin, String target, int cnt){
        if(begin.equals(target)){
            min_cnt = Math.min(min_cnt, cnt);
            return;
        }
        for(int i = 0; i < share_words.length; i++){
            if(checked[i] == true) continue;
            int dif = 0;
            for(int j = 0; j < share_words[i].length(); j++){
                if(dif > 1)
                    break;
                if(begin.charAt(j) != share_words[i].charAt(j)){
                    dif++;
                }
            }
            if(dif == 1){
	            //그리고 돌아갈 때를 잘 구별해놓기
	            String tmp = begin;
                begin = share_words[i];
                checked[i] = true;
                dfs(begin, target, cnt+1);
                begin = tmp;
                checked[i] = false;
            }
        }
    }
}