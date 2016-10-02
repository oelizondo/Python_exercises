from node import Node

class LinkedList:
  def __init__(self):
    self.head = None
    self.length = 0

  def add(self, data):
    if self.head is None:
      self.head = Node(data)
      self.increment()
    else:
      self._add_node(data)

  def erase(self, data):
    if self.head.data == data:
      self.head = self.head.next
      self.decrement()
    else:
      self._erase_node(data)

  def invert(self):
    temp = self.head
    stack = []
    while temp.next is not None:
      stack.append(temp.data)
      temp = temp.next

    temp = self.head
    for i in range(len(stack)):
      temp.data = stack[(len(stack)-1)-i]
      temp = temp.next

  def map(self, function):
    self._map(self.head, function)

  def _map(self, node, function):
    if node is None:
      return
    else:
      node.data = function(node.data)
      self._map(node.next, function)

  def reduce(self, operator):
    if operator == "+":
      return self._sum_list()
    elif operator == "*":
      return self._multiply_list()
    else
      return False

  def _sum_list(self):
    accumulator = 0
    temp = self.head
    while temp is not None:
      accumulator += temp.data
      temp = temp.next
    return accumulator

  def _multiply_list(self):
    accumulator = 1
    temp = self.head
    while temp is not None:
      accumulator *= temp.data
      temp = temp.next
    return accumulator

  def _erase_node(self, data):
    temp = self.head
    while temp.next is not None:
      if temp.next.data == data:
        temp.next = temp.next.next
        self.decrement()
      else:
        temp = temp.next

  def _add_node(self, data):
    temp = self.head
    while temp.next is not None:
      temp = temp.next
    temp.next = Node(data)
    self.increment()

  def print_list(self):
    temp = self.head
    while temp is not None:
      print(temp.data)
      temp = temp.next
  def selfie(self):
    return self

  def increment(self):
    self.length += 1
  def decrement(self):
    self.length -= 1