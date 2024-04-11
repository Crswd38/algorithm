class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String[] ms = my_string.split("");
        String[] os = overwrite_string.split("");
        String answer = "";
        for(int i=0; i<os.length; i++){
            ms[i+s] = os[i];
        }
        StringBuilder sb = new StringBuilder();
        for(int i=0; i<ms.length; i++){
            sb.append(ms[i]);
        }
        answer = sb.toString();
        return answer;
    }
}