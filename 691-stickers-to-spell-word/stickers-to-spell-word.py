from collections import Counter
import math
import functools

class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        sticker_counters = [Counter(s) for s in stickers]
        memo = {}

        def dfs(word):
            if word == "":
                return 0
            if word in memo:
                return memo[word]

            word_cntr = Counter(word)
            res = float('inf')

            for sticker_cntr in sticker_counters:
                if word[0] not in sticker_cntr:
                    continue

                remaining = word_cntr - sticker_cntr
                remaining_word = "".join(sorted(remaining.elements()))
                remaining_need = dfs(remaining_word)

                if remaining_need != -1:
                    res = min(res, remaining_need)

            memo[word] = 1 + res if res != float('inf') else -1
            return memo[word]

        return dfs(target)
