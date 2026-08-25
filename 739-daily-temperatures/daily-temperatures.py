class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack =[]
        ans=[]
        i=len(temperatures)-1
        stack.append(i)
        ans.append(0)
        i-=1
        j=0

        while i >= 0:
            while stack and temperatures[stack[j]] <= temperatures[i]:
                stack.pop()
                j-=1
            if len(stack)==0:
                ans.append(0) 
            else:
                ans.append(stack[-1]-i)

            stack.append(i)
            j+=1
            i-=1
        ans.reverse()
            
        return ans
            