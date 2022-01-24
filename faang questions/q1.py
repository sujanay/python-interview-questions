# This question was recently asked by Google. Given two sorted linked lists, merge them in order.

# Definition for a linked-list node.
class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

class Solution:
  def mergeTwoLists(self, a, b):
    #
    # Fill this in.
    #

# Test program
# 1 -> 3 ->5
a = Node(1)
a.next = Node(3)
a.next.next = Node(5)

# 2 -> 4 -> 6
b = Node(2)
b.next = Node(4)
b.next.next = Node(6)

c = Solution().mergeTwoLists(a, b)
while c:
  print(c.val)
  c = c.next
# 1 2 3 4 5 6

"""
See the solution
This problem can be solved recursively or iteratively. We traverse the two linked lists in parallel, 
advancing both pointers simultaneously. If the first list's value is smaller we advance that one, 
otherwise we advance the second list. If either list is shorter, then we take values from the longer list.

The time complexity is linear O(n) since both lists are traversed just once. The space complexity of the
recursive algorithm is linear O(n), since it builds up a recursive stack that may be as deep as the length of
both lists. The space complexity of the iterative solution is constant O(1), since only a few variables are used.
"""

# Definition for a linked-list node.
class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

class Solution:
  def mergeTwoLists(self, a, b):
    if a is None:
      return b
    elif b is None:
      return a
    elif a.val < b.val:
      a.next = self.mergeTwoLists(a.next, b)
      return a
    else:
      b.next = self.mergeTwoLists(a, b.next)
      return b

  def mergeTwoListsIterative(self, a, b):
    node = None
    head = None
    while True:
      if a is None:
        nextNode = b
      elif b is None:
        nextNode = a
      elif a.val < b.val:
        nextNode = a
      else:
        nextNode = b

      if nextNode == a:
        a = a.next if a else None
      if nextNode == b:
        b = b.next if b else None

      if nextNode is None:
        break
      if not node:
        node = nextNode
        head = node
      else:
        node.next = nextNode
      node = nextNode
    return head

# Test program
# 1 -> 3 ->5
a = Node(1)
a.next = Node(3)
a.next.next = Node(5)

# 2 -> 4 -> 6
b = Node(2)
b.next = Node(4)
b.next.next = Node(6)

c = Solution().mergeTwoLists(a, b)
while c:
  print(c.val)
  c = c.next
# 1 2 3 4 5 6
