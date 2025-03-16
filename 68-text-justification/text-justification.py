class Solution(object):
    def fullJustify(self, words, maxWidth):
        res = []  # Stores the final justified lines
        cur = []  # Stores words for the current line
        cur_len = 0  # Total length of words in the current line

        for word in words:
            # Check if adding a new word would exceed maxWidth
            if cur_len + len(word) + len(cur) > maxWidth:
                # Distribute spaces
                for i in range(maxWidth - cur_len):
                    cur[i % (len(cur) - 1 or 1)] += ' '  
                res.append("".join(cur))  # Add the justified line to result
                cur, cur_len = [], 0  # Reset for new line

            cur.append(word)
            cur_len += len(word)

        # Last line (left-justified)
        res.append(" ".join(cur).ljust(maxWidth))
        return res


solution = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

output = solution.fullJustify(words, maxWidth)
for line in output:
    print '"' + line + '"'  
