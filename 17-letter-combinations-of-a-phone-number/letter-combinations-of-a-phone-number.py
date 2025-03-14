class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        result = []
        
        def backtrack(index, current_combination):
            if index == len(digits):
                result.append("".join(current_combination))
                return
            
            for letter in phone_map[digits[index]]:
                current_combination.append(letter)
                backtrack(index + 1, current_combination)
                current_combination.pop()
        
        backtrack(0, [])
        return result


sol = Solution()
print(sol.letterCombinations("23")) 
print(sol.letterCombinations(""))   
print(sol.letterCombinations("2"))   
