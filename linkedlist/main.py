from linkedlist import LinkedList

myLL = LinkedList()
myLL.add(10)
myLL.add(11)
myLL.add(12)
myLL.add(13)
myLL.erase(10)
myLL.add(14)
myLL.add(15)
# myLL.invert()
myLL.print_list()
square = lambda x: x * x
myLL.map(square)
# myLL.print_list()

print(myLL.selfie())
print(myLL.reduce("+"))
print(myLL.reduce("*"))
print(myLL.length)