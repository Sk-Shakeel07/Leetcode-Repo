class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort(reverse=True)
        trainers.sort(reverse=True)
        count = 0
        while players and trainers:
            if players[-1] <= trainers[-1]:
                players.pop()
                count += 1
            trainers.pop()
        return count