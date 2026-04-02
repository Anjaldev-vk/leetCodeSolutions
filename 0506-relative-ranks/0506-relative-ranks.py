class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sort_scr = sorted(score, reverse = True)
        rank = {}
        for i,v in enumerate(sort_scr):
            if i == 0:
                rank[v] = "Gold Medal"
            elif i == 1:
                rank[v] = "Silver Medal"
            elif i ==2 :
                rank[v] = "Bronze Medal"
            else:
                rank[v] = str(i+1)
        result = []
        for v in score:
            result.append(rank[v])
        return result
        
    
         
        