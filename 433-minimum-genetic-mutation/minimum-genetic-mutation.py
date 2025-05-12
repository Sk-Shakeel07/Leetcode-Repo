class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        bankSet = set(bank)
        if endGene not in bankSet:
            return -1

        kGenes = 'ACGT'
        q = collections.deque([startGene])
        step = 1

        while q:
            for _ in range(len(q)):
                wordList = list(q.popleft())
                for j in range(len(wordList)):
                    cache = wordList[j]
                    for c in kGenes:
                        wordList[j] = c
                        word = ''.join(wordList)
                        if word == endGene:
                            return step
                        if word in bankSet:
                            bankSet.remove(word)
                            q.append(word)
                    wordList[j] = cache
            step += 1

        return -1
