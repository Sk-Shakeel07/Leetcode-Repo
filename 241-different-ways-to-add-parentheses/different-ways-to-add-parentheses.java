import java.util.*;

class Solution {
    // Cache to memoize results of subexpressions
    private Map<String, List<Integer>> memo = new HashMap<>();
    
    public List<Integer> diffWaysToCompute(String expression) {
        // If already computed, return cached result
        if (memo.containsKey(expression)) {
            return memo.get(expression);
        }

        List<Integer> result = new ArrayList<>();
        
        for (int i = 0; i < expression.length(); i++) {
            char ch = expression.charAt(i);
            
            if (ch == '+' || ch == '-' || ch == '*') {
                // Divide
                String leftExpr = expression.substring(0, i);
                String rightExpr = expression.substring(i + 1);

                List<Integer> leftResults = diffWaysToCompute(leftExpr);
                List<Integer> rightResults = diffWaysToCompute(rightExpr);

                // Conquer
                for (int left : leftResults) {
                    for (int right : rightResults) {
                        int val = 0;
                        switch (ch) {
                            case '+': val = left + right; break;
                            case '-': val = left - right; break;
                            case '*': val = left * right; break;
                        }
                        result.add(val);
                    }
                }
            }
        }

        // Base case: no operator found
        if (result.isEmpty()) {
            result.add(Integer.parseInt(expression));
        }

        // Memoize and return
        memo.put(expression, result);
        return result;
    }
}
