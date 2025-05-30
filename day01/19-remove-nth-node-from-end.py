
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        f=head
        b=head
        for i in range(n):
            f=f.next
        if f is None:
            return head.next
        while f.next:
            b=b.next
            f=f.next
        b.next=b.next.next
        return head