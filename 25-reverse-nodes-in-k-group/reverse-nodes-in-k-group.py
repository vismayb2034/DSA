# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        left = head
        
        prevleft = None
        res = None

        while left:
            n=k
            right = left
            for i in range(1,k) :
                if right.next==None:
                    right=None
                    break
                right=right.next

            
            if right:
                nxtleft=right.next
                prev=None
                curr=left
                while n:
                    nxt = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nxt
                    n-=1
                if prevleft:
                    prevleft.next=right
                prevleft=left
                left=nxtleft
                if res==None:
                    res=right
                
            else:
                if prevleft:
                    prevleft.next = left
                else:
                    res = left
                break
        return res 
                
                    

