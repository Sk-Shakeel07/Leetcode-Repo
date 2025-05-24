class Solution(object):
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """
        dictionary.sort(key=lambda x: (-len(x), x))  # sort by length descending, then lexicographically
        for word in dictionary:
            i = 0
            for c in s:
                if i < len(word) and word[i] == c:
                    i += 1
            if i == len(word):  # if we have matched all characters of word
                return word
        return ""
