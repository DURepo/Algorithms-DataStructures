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



#Stack using two queues
#https://www.geeksforgeeks.org/implement-stack-using-queue/

class stackUsingQueues():
  def __init__(self):
    self.q1 = queue()
    self.q2 = queue()

  def push(self, ele):
    self.q2.enqueue(ele)

    n = self.q1.size()
    i = 0
    while(i<n):
      tempEle = self.q1.dequeue()
      self.q2.enqueue(tempEle)

      i +=1
    
    temp = self.q1
    self.q1 = self.q2
    self.q2 = temp

  def pop(self):
    return self.q1.dequeue()


sq = stackUsingQueues()

sq.push('A')
sq.push('B')
print(sq.pop())







    





  