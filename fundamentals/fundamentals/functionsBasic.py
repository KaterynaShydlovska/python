def countdown(n):
  list = [];
  while n >= 0:
    list.append(n)
    n = n-1
  return list

print(countdown(5))

def rint_and_Return(list):
  print(list[0])
  return list[1]

print(rint_and_Return([5, 4]))

def First_Plus_Length(list):
  return list[0]+ len(list)
 
print(First_Plus_Length([5, 4]))

def ValuesGreater_than_Second(list):
  newList=[]
  for n in list:
    if(n > list[1]):
      newList.append(n)
  print(len(newList))
  return newList

print(ValuesGreater_than_Second([5, 4, 2, 10, 8]))

def ValuesGreater_than_Second(list):
  if len(list) <= 1:
    return False
    
  newList=[]
  for n in list:
    if(n > list[1]):
      newList.append(n)
  print(len(newList))
  return newList

print(ValuesGreater_than_Second([5, 4, 2, 10, 8]))

def length_and_value(l, val):
  list = []
  size=0;
  while size < l:
    list.append(val)
    size = size+1
  return list

print(length_and_value(6,2))