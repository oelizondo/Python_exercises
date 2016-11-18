from node import Node

class Double:
  def __init__(self):
    self.head = None
    self.tail = None

  def add(self, data):
    if self.head == None:
      self.add_head(data)
    else:
      self.add_node(data)

  def add_head(self, data):
    self.head = Node(data)

  def add_node(self, data):
    temp = self.head
    while temp.next is not None:
      temp = temp.next
    temp.next = Node(data)
    temp.next.prev = temp
    self.tail = temp.next

  def erase(self, data):
    if(self.head.data == data):
      self.erase_head(data)
    else:
      self.erase_node(data)

  def erase_head(self, data):
    self.head = self.head.next
    self.head.prev = None

  def erase_node(self, data):
    temp = self.head
    aux = self.head
    while temp.next.data != data:
      temp = temp.next
      aux = aux.next
    temp.next = temp.next.next
    temp.next.prev = aux

  def print_r(self):
    temp = self.head
    while temp is not None:
      print(temp.data)
      temp = temp.next

  def print_l(self):
    temp = self.tail
    while temp is not None:
      print(temp.data)
      temp = temp.prev
