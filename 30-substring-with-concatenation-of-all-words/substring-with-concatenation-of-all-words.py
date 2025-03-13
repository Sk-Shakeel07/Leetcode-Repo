from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        word_freq = Counter(words)
        result = []

        # Iterate over each possible starting point within word_len range
        for i in range(word_len):
            left, right = i, i
            seen = Counter()
            count = 0

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in word_freq:
                    seen[word] += 1
                    count += 1

                    # If a word appears too many times, shrink the window
                    while seen[word] > word_freq[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1

                    # If we match exactly, store the index
                    if count == word_count:
                        result.append(left)
                else:
                    seen.clear()
                    count = 0
                    left = right  # Reset window

        return result


s = "barfoofoobarthefoobarman"
words = ["bar", "foo", "the"]
solution = Solution()
print(solution.findSubstring(s, words))  
