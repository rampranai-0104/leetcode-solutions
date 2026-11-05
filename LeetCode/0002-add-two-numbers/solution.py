# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        h1=l1#self.rev(l1)
        h2=l2#self.rev(l2)
        carry=0
        d=ListNode(-1)
        ref=d
        while (h1!=None or h2!=None or carry!=0):
            x=h1.val if h1!=None else 0
            y=h2.val if h2!=None else 0
            s=(x+y+carry)
            carry=s//10
            node=ListNode(s%10)
            ref.next=node
            ref=node
            h1=h1.next if h1!=None else None
            h2=h2.next if h2!=None else None
        return d.next
   

