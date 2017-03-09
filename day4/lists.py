
 def find_missing(list1,list2):
  if list1==list2:
    print 0
  for i in list1:
    if i in list2:
      print [i]
    if i not in list2: # and list1==list2:
      print [i]