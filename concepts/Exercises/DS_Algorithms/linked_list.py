class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while (printval):
            print(printval.dataval),
            printval = printval.nextval

    def AtBegining(self,newdata):
        NewNode = Node(newdata)
        # Update the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode

    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

    def RemoveNode(self, Removekey):

        HeadVal = self.headval

        if (HeadVal is not None):
            if (HeadVal.dataval == Removekey):
                self.headval = HeadVal.nextval
                HeadVal = None
                return

        while (HeadVal is not None):
            if HeadVal.dataval == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.nextval

        if (HeadVal == None):
            return

        prev.nextval = HeadVal.nextval

        HeadVal = None

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list.listprint()
list.AtBegining("Sun")

list.listprint()
list.AtEnd("Thu")

list.listprint()
list.Inbetween(list.headval.nextval,"Fri")

list.listprint()
llist = SLinkedList()
llist.AtBegining("Mon")
llist.AtBegining("Tue")
llist.AtBegining("Wed")
llist.AtBegining("Thu")
llist.RemoveNode("Tue")
llist.listprint()
