import java.util.*;
class Solution {
// 여행경로
static boolean[] check;
	static boolean[] wrong_check;
 	static String[][] tickets_clone;
	static List<String> result_list;
	static List<String> temp_list;
	static boolean isFinished = false;
    public String[] solution(String[][] tickets) {
        check = new boolean[tickets.length];
        Arrays.sort(tickets, new Comparator<String[]>(){
            @Override
            public int compare(String[] a, String[] b){
                return a[1].compareTo(b[1]);
            }
        });
        tickets_clone = tickets.clone();
        result_list = new ArrayList<>();
        temp_list = new ArrayList<>();
        // 잠만 생각을 해보자 ICN에서 출발을 해 그럼 ICN에서 젤 작은 걸 골라야되
        // 그런 다음에 다시 그 출발지에서 가장 오름차순인걸 골라야 되... 그런 식으로 계속 반복해서 
        // 다 체크를 해야 끝나는 거잖아...
        dfs("ICN", 0);
        String[] answer = new String[result_list.size()];
        for(int i = 0; i < result_list.size(); i++) {
        	answer[i] = result_list.get(i);
        }
        return answer;
    }
    public void dfs(String from, int num) {
    	temp_list.add(from);
        if (num == tickets_clone.length) {
            if (!isFinished) { // 첫 번째 완성된 경로를 최종 결과로 저장
                result_list.addAll(temp_list);
                isFinished = true;
            }
            temp_list.remove(temp_list.size() - 1); // 백트래킹을 위해 마지막 추가한 경로 제거
            return;
        }
        for (int i = 0; i < tickets_clone.length; i++) {
            if (tickets_clone[i][0].equals(from) && !check[i]) {
                check[i] = true;

                dfs(tickets_clone[i][1], num + 1);

                check[i] = false; // 백트래킹을 위해 체크 상태 복원
            }
        }

        temp_list.remove(temp_list.size() - 1);
    }
}