class Solution {
    public String replaceWords(List<String> dictionary, String sentence) {
        String arr[] = sentence.split(" ");
        Collections.sort(dictionary, (a, b) -> a.length() - b.length());
        String str="";
        for(int i=0;i<arr.length;i++){
            for(int j=0;j<dictionary.size();j++){
                if(arr[i].startsWith(dictionary.get(j))){
                    arr[i]=dictionary.get(j);
                    break;
                }
            }
            str+=arr[i]+" ";
        }
        return str.trim();
    }
}