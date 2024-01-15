class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        noloss = []
        oneloss = []
        
        losses = defaultdict(int)
        
        players = set()
        
        for match in matches:
            losses[match[1]] += 1
            players.add(match[0])
            players.add(match[1])
        
        players = sorted(players)
        
        for player in players:
            if losses[player] == 0:
                noloss.append(player)
            elif losses[player] == 1:
                oneloss.append(player)
        
        return [noloss, oneloss]
