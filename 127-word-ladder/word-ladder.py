from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)  # Convert wordList to a set for O(1) lookups
        if endWord not in wordSet:
            return 0
        
        # Initialize two sets for bidirectional search
        frontSet = {beginWord}
        backSet = {endWord}
        visited = set()
        length = 1
        
        while frontSet and backSet:
            # Always expand the smaller set to optimize performance
            if len(frontSet) > len(backSet):
                frontSet, backSet = backSet, frontSet
            
            nextSet = set()
            for word in frontSet:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:i] + c + word[i+1:]
                        
                        if newWord in backSet:  # If paths meet, return the result
                            return length + 1
                        
                        if newWord in wordSet and newWord not in visited:
                            nextSet.add(newWord)
                            visited.add(newWord)
            
            frontSet = nextSet
            length += 1
        
        return 0  # No transformation sequence found

sol = Solution()
print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))  
print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))        
