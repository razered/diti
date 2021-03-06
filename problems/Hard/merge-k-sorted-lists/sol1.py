# Definition for singly-linked list.
from typing import List

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

	def __repr__(self):
		if self.next:
			return f'{self.val} {self.next}'
		else:
			return f'{self.val}'

class Solution:
	def mergeKLists(self, lists):
		if any(lists):
			next = min((head.val, i) for i, head in enumerate(lists) if head is not None)[1]
			new_heads = [head.next if i == next else head for i, head in enumerate(lists) if head is not None]
			lists[next].next = self.mergeKLists(new_heads)
			return lists[next]
		else: 
			return None

# lists = [[1,4,5],[1,3,4],[2,6]]
lists = [ListNode(1, ListNode(4, ListNode(5))),
		 ListNode(1, ListNode(3, ListNode(4))), 
		 ListNode(2, ListNode(6))]

print(Solution().mergeKLists(lists))
# print(Solution().reverseTCO(ListNode(1, ListNode(4, ListNode(5))), None))