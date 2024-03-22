class Solution {
    public int solution(String name) {
        int answer = 0;
        int minMove = name.length()-1;
        for(int i = 0; i < name.length(); i++) {
            answer += getIdxMove(name, i); // 상하 조작 횟수 더하기
            int next = i + 1;
            // 연속된 A 문자열들 건너뛰기
            while(next < name.length() && name.charAt(next) == 'A') {
                next++;
            }

                        minMove = Math.min(minMove, i*2 + (name.length() - next));
            minMove = Math.min(minMove, (name.length() - next)*2 + i);
        }
        answer += minMove;
        return answer;
    }
    public int getIdxMove(String name, int idx) {
        int answer = 0;
        int Z_idx = (int)'Z';
        int ASCIIalpha = (int) name.charAt(idx);
        int differ = ASCIIalpha - (int) 'A';
        int reverse_differ = Z_idx - ASCIIalpha + 1;
        answer = Math.min(differ, reverse_differ);
        return answer;
    }
}