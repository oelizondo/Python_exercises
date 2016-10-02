from node import Node

class Tree:
  def __init__(self):
    self.root = None
    self.nodes = 0

  def add(self, data):
    if self.root == None:
      self.root = Node(data)
    else:
      self._add_node(self.root, data)

  def _add_node(self, node, data):
    if node.data > data and node.right is not None:
      _add_node(node.right, data)
    elif node.data < data and node.left is not None:
      _add_node(node.left, data)
    elif node.data > data and node.right is None:
      node.right = Node(data)
    elif node.data < data and node.left is None:
      node.left = Node(data)
    else:
      return False

  def print_tree(self):
    self._print(self.root)

  def _print(self, node):
    if node is not None:
      self._print(node.right)
      print(node.data)
      self._print(node.left)