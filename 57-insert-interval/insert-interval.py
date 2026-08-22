class Solution(object):
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        j=0

        s1=intervals[0][0]
        e1=intervals[0][1]
        for i in range(1,len(intervals)):
            s2=intervals[i][0]
            e2=intervals[i][1]

            if e1>=s2:
                e1=max(e1,e2)

            else:
                intervals[j][0]=s1
                intervals[j][1]=e1
                j+=1

                s1=s2
                e1=e2

        intervals[j][0]=s1
        intervals[j][1]=e1
        j+=1

        del intervals[j:]

        return intervals
