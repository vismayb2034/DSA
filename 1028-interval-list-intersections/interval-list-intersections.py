class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        res=[]
        n=len(firstList)
        m=len(secondList)
        i=j=0
        while(i<n and j<m):
            s1=firstList[i][0]
            e1=firstList[i][1]
            s2=secondList[j][0]
            e2=secondList[j][1]

            if s1<s2:
                if e1>=s2:
                    a=max(s1,s2)
                    b=min(e1,e2)
                    res.append([a,b])
            else:
                if e2>=s1:
                    a=max(s1,s2)
                    b=min(e1,e2)
                    res.append([a,b])
            
            if e1<=e2:
                i+=1
            else:
                j+=1
        return res
