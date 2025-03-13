import java.util.*;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagramMap = new HashMap<>();
        
        for (String s : strs) {
            // Convert string to character array, sort it, and create a key
            char[] charArray = s.toCharArray();
            Arrays.sort(charArray);
            String sortedStr = new String(charArray);
            
            // Add the string to the corresponding group
            anagramMap.computeIfAbsent(sortedStr, k -> new ArrayList<>()).add(s);
        }
        
        return new ArrayList<>(anagramMap.values());
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        
        
        String[] input1 = {"eat", "tea", "tan", "ate", "nat", "bat"};
        System.out.println(solution.groupAnagrams(input1));
        
        
        String[] input2 = {""};
        System.out.println(solution.groupAnagrams(input2));

        
        String[] input3 = {"a"};
        System.out.println(solution.groupAnagrams(input3));
    }
}
