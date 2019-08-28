#Queue in python using list

class queue():
  def __init__(self):
    self.items =[]

  def isempty(self):
    return len(self.items)>0

  def enqueue(self, ele):
    self.items.insert(0, ele)

  def dequeue(self):
    return self.items.pop()

  def size(self):
   return len(self.items)


# q = queue()
# q.enqueue(1)
# print(q.size())
# print(q.isempty())
# q.enqueue(2)
# print(q.size())
# q.dequeue()





#https://www.geeksforgeeks.org/implement-a-stack-using-single-queue/
class stackUsingQueue():
  def __init__(self):
    self.q = queue()

  def push(self, ele):

    n = self.q.size()
    print(n)
    self.q.enqueue(ele)
    i=0
    while(i<n):
      k = self.q.dequeue()
      self.q.enqueue(k)
      i+=1

  
  def pop(self):
    return self.q.dequeue()

  def size(self):
    return self.q.size()


sq = stackUsingQueue()

sq.push('A')
print('SIZE: ', sq.size())
sq.push('B')

print('SIZE: ', sq.size())
print(sq.pop())

    





  