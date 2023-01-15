class Node:
    def __init__(self,data=None,next=None,prev=None):
      self.data = data
      self.next = next
      self.prev = prev



class Linked_list:
  def __init__(self) :
      self.head = None


  def insert_at_beginning(self,data):
    node = Node(data,self.head)
    self.head = node


  def insert_at_end(self,data):
    if self.head is None:
      self.head = Node(data)
      return

    itr = self.head

    while itr.next:
      itr = itr.next

    itr.next = Node(data,None,itr)



  def insert_at(self,index,data):
    if index < 0 and index >= self.get_length():
      raise Exception("Invalid Index")

    if index == 0:
      self.insert_at_beginning(data)
      return
    

    count  = 0
    itr = self.head

    while itr:
      if count == index - 1:
        node = Node(data,itr.next,itr)
        itr.next = node
        break


      itr = itr.next
      itr.prev = itr
      count += 1


  def remove_at(self,index):
    if index < 0 or index >= self.get_length():
      raise Exception('This is not a valid index')

    if index == 0:
      self.head = self.head.next
      self.prev = None
      return
    
    count = 0
    itr = self.head

    while itr:
      if count == index - 1:
        itr.next = itr.next.next
        itr.next.prev = itr
        break
      itr = itr.next
      count += 1


  def get_length(self):
    count = 0
    itr = self.head
    while itr:
      count += 1
      itr = itr.next

    return count

  
  def insert_new_values(self,data_list):
    self.head = None
    for data in data_list:
      self.insert_at_end(data)


  def insert_after(self,prev,data): 
    itr = self.head

    while itr:
      if itr.data == prev:
        node = Node(data,itr.next,itr)
        itr.next = node
        break
      
      itr = itr.next


  def insert_before(self,next,data):
    itr = self.head

    count = 0

    while itr:
      if count == 0 and itr.data == next:
        node = Node(data,itr)
        itr.prev = node
        break

      if itr.data == next:
        node = Node(data,itr,itr.prev)
        itr.prev.next = node
        itr.prev = node
        break

      itr = itr.next
      count += 1

  
  def delete_before(self,next):
    itr = self.head

    if self.get_length() <=1: 
      raise Exception('Cant remove an element before an element in an list with less or equal to 1 element')

    while itr:
      if itr.data == next:
        itr.prev = itr.prev.prev
        itr.prev.next = itr
        break

      itr = itr.next
        
  
  def delete_after(self,prev):
    itr = self.head

    while itr:
      if itr.data == prev:
        itr.next = itr.next.next
        itr.next.prev = itr
        break

      if itr.next == None:
        raise Exception(f'{prev} not found in linked List')

      itr = itr.next


  def print(self):
    itr = self.head

    if itr is None:
      print("Linked list is empty")
      return
      
    llstr = ''

    count = 0

    while itr:
      if count == self.get_length() - 1:
        llstr += str(itr.data)
      else:
        llstr += str(itr.data) + '<-->'

      itr = itr.next
      count += 1

    print(llstr)


if __name__ == '__main__':
  ll = Linked_list()
  ll.print()
