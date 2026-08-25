class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack =[]
        ans=[]
        i=len(temperatures)-1
        stack.append(i)
        ans.append(0)
        i-=1
        

        while i >= 0:
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
                
            if len(stack)==0:
                ans.append(0) 
            else:
                ans.append(stack[-1]-i)

            stack.append(i)
            
            i-=1
        ans.reverse()
            
        return ans
            