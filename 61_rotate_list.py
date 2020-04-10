# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or head is None:
        	return head
        end = head
        newEnd = head
        distance = 0
        while distance < k:
        	distance += 1
        	if end.next is None and distance > 0:
        		k = k % distance
        		return self.rotateRight(head, k)
        	end = end.next
        	# distance += 1
        while end.next is not None:
        	end = end.next
        	newEnd = newEnd.next
        end.next = head
        newHead = newEnd.next
        newEnd.next = None
        return newHead

one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)

one.next = two
two.next = three
three.next = four
four.next = five

s = Solution()
res = s.rotateRight(one, 2)
assert res.val == 4

zero = ListNode(0)
one = ListNode(1)
two = ListNode(2)
zero.next = one
one.next = two
res2 = s.rotateRight(zero, 4)
assert res2.val == 2