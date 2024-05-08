class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        '''ans=[0]*len(score)
        i=0
        for ele in score:
            m=max(score)
            while i<3:
                if i==0: ans[score.index(m)]="Gold Medal"
                if i==1: ans[score.index(m)]="Silver Medal"
                if i==2: ans[score.index(m)]="Bronze Medal"
                i+=1
            ans[score.index(m)]=str(i+1)
            score.pop()
        return ans'''
      
        scoreMap={score[i]: i for i in range(len(score))}
        score.sort(reverse=True)
        result=["" for _ in range(len(score))]
        for i in range(len(score)):
            if i == 0:
                result[scoreMap[score[i]]] = "Gold Medal"
            elif i == 1:
                result[scoreMap[score[i]]] = "Silver Medal"
            elif i == 2:
                result[scoreMap[score[i]]] = "Bronze Medal"
            else:
                result[scoreMap[score[i]]] = str(i + 1)

        return result           
