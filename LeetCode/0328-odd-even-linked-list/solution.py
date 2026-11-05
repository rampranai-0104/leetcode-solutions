# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        oddD=ListNode(-1)
        evenD=ListNode(-1)
        od=oddD
        ed=evenD
        x=1
        while (head!=None):
            if x & 1 ==1:
                od.next=head
                od=head
            else:
                ed.next=head
                ed=head
            head=head.next
            x+=1
        od.next=evenD.next
        ed.next=None
        return oddD.next
