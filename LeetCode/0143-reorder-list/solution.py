# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return 
        mid=self.findmid(head)
        nn=mid.next
        mid.next=None
        rh=self.reverse(nn)
        return self.join(head,rh)

    def findmid(self,head):
        s=head
        f=head
        while (f.next!=None and f.next.next !=None):
            f=f.next.next
            s=s.next
        return s 

    def join(self,h,rh):
        while (h!=None and rh!=None):
            t1=h.next
            h.next=rh
            t2=rh.next
            rh.next=t1
            h=t1
            rh=t2
    def reverse(self,head):
        prev=None
        temp=head
        while temp:
            nxt=temp.next
            temp.next=prev
            prev=temp
            temp=nxt
        return prev
