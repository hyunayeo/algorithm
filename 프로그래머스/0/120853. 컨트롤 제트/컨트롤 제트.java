class Solution {
    public int solution(String s) {
        int answer = 0;
        String[] arr = s.split(" ");
        for(int i=arr.length-1; i>=0; i--){
            if(arr[i].equals("Z")){
                i=i-1;
            }else{
                answer = answer + Integer.parseInt(arr[i]);
            }
        }
        return answer;
    }
}