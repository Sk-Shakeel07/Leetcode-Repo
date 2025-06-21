class Solution {
    public boolean isValid(String code) {
        
        Stack<String> stack = new Stack<>(); // TAG_NAME is pushed to stack
        
        for(int i = 0; i < code.length();){
            
            if(i>0 && stack.isEmpty()) // No TAG_NAME found in the beginning 
                return false;
            
            // <![CDATA[ begin for <![CDATA[CDATA_CONTENT]]>
            // CDATA_CONTENT may contain any characters and is not checked
            if(code.startsWith("<![CDATA[", i)){
                int j = i+9;
                i = code.indexOf("]]>", j);
                if(i < 0) //if not found "]]>"
                    return false;
                i += 3;
            }
            
            // </TAG_NAME> end
            else if(code.startsWith("</", i)){
                int j = i + 2;
                i = code.indexOf('>', j);
                if(i < 0 || i == j || i - j > 9) 
                    return false;
                for(int k = j; k < i; k++){
                    if(!Character.isUpperCase(code.charAt(k)))  // TAG_NAME only contain upper-case letters
                        return false;
                }
                String s = code.substring(j, i++);
                if(stack.isEmpty() || !stack.pop().equals(s)) // TAG_NAME doesn't match
                    return false;
            }
            
            // <TAG_NAME> begin
            else if(code.startsWith("<", i)){
                int j = i + 1;
                i = code.indexOf('>', j);
                // i < 0  => No '>' found
                // i == j => Instead of <TAG_NAME> just found <>
                //  i - j > 9  => TAG_NAME has length in range [1,9]
                if(i < 0 || i == j || i - j > 9) 
                    return false;
                for(int k = j; k < i; k++){
                    if(!Character.isUpperCase(code.charAt(k))) //TAG_NAME only contain upper-case letters
                        return false;
                }
                String s = code.substring(j, i++);
                stack.push(s);
            }
            
            // All other characters
            else{
                i++;
            }
        }
        return stack.isEmpty();
    }
}