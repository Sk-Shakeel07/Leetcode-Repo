class Solution:
    def wordBreak(self, s, wordDict):
        dp = [None for i in range(len(s))]
        res = [False]
        
        def fun(index):
            if index >= len(s):
                res[0] = True
                return True
            if dp[index] is not None:
                return dp[index]
            for each in wordDict:
                if s[index:len(each) + index] == each:
                    if fun(index + len(each)):
                        dp[index] = True
                    else:
                        dp[index] = False
        
        fun(0)
        return res[0]