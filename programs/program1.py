# Write a python program that takes two lists and returns True if they have at least one common member.

list1 = [1,2,3,'A',5,'C']
list2 = [22,'D',11,55,85]

def common(list1,list2):
  lst_cmn = []
  for i in list1:
    if i in list2:
      lst_cmn.append(i)
      return True
  else:
    return False


result = common(list1, list2)
print(result)
