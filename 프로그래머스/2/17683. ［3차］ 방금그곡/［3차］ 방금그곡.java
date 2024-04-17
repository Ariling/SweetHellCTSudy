class Solution {
	static int time;
	static String result;
    public String solution(String m, String[] musicinfos) {
        String answer = "";
        // C#과 같은 음을 소문자로 치환 
        m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a").replace("B#","b");
        time = 0;
        result = "";
        for(int i = 0; i < musicinfos.length; i++) {
        		String[] arr = musicinfos[i].split(",");
        		String[] start_arr = arr[0].split(":");
        		String[] end_arr = arr[1].split(":");
        		String melody = arr[3].replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a").replace("B#","b");
        		int start = (60 * Integer.parseInt(start_arr[0])) + Integer.parseInt(start_arr[1]);
        		int end = (60 * Integer.parseInt(end_arr[0])) + Integer.parseInt(end_arr[1]);
        		int dif = end - start;
        		StringBuilder str = new StringBuilder();
        		for(int j = 0; j < dif; j++) {
        			str.append(melody.charAt(j % melody.length()));
        		}
        		if(str.toString().contains(m) && dif > time) {
        			time = dif;
        			result = arr[2];
        		}
        	}
        answer = result == "" ? "(None)" : result;
        return answer;
    }
}