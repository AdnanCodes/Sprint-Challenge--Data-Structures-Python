class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    # TO BE COMPLETED
    
    #track the current node
    current = self.head
    #track the previous node when current moves
    previous = None

    #set next pointer after current and check for empty list
    if current:
        next_to_reverse = current.get_next()

    #Current needs to move through and flip the pointers to previous

    while current != None:
        #Switch pointers
        current.set_next(previous)
        previous = current
        current = next_to_reverse
        #check if next node exists otherwise it is end of list
        if next_to_reverse != None:
            next_to_reverse = next_to_reverse.get_next()
      
    #After loop completes, previous will have last node isn't pointed backwards 
    self.head = previous