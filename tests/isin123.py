def isin1 (l, p):
  """ 
  есть ли в списке l элемент p
  l - список, в котором ищем
  p - искомый элемент
  """
  for i in range(0, len(l)):
    if l[i] == p:
      return True
  return False

def isin2 (l, p):
  for e in l:
    if e == p:
      return True
  return False

def isin3 (l, p):
  return p in l

s = [1, 2, 3]
print(s)

print (isin3 (s, 1))
print (isin3 (s, 111))
print (isin3 (s, 0))


