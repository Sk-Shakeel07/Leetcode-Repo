class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        mp = Counter(s)
        r = OrderedDict(sorted(mp.items(), key=lambda x: x[1], reverse=True))
        ss = ''.join([char * freq for char, freq in r.items()])
        return ss
