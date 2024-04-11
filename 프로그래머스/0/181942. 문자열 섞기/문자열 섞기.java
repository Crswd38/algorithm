class Solution {
    public String solution(String str1, String str2) {
        String[] arr1 = str1.split("");
        String[] arr2 = str2.split("");
        StringBuilder sb = new StringBuilder();
        for(int i=0; i<arr1.length; i++){
            sb.append(arr1[i]+arr2[i]);
        }
        String answer = sb.toString();
        return answer;
    }
}