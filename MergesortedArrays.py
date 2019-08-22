# https://www.geeksforgeeks.org/merge-two-sorted-arrays/

a = [ 1, 3, 4, 5]
b = [2, 4, 6, 8]

a= [ -5, 8, 9]
b =[4, 7, 8]

def mergeArray(a,b):
  n = len(a)
  m = len(b)
  c =  [0] *(n + m)

  i = 0
  j = 0


  if(n ==0 and m==0):
    return []
  
  elif(n==0):
    return b
  
  elif(m==0):
    return a

  for k in range(m+n):
    if(a[i] <= b[j]):
      c[k] = a[i]
      if(i==n-1): break
      else: i+=1

    else:
      c[k] = b[j]
      if(j==n-1): break
      else: j+=1

  k+=1
  if(i<n and j==m-1):
    for x in range (i,n):
      c[k] = a[x]
      k +=1
    return c
  elif(i==n-1 and j<m):
    for x in range(j,m):
      c[k] = b[x]
      k+=1
    return c
  else:
    return c



print(mergeArray(a,b))
    