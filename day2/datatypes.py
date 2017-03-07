def data_type(i):
  if type (i)==str:
    return len(i)
    
  elif type(i)==bool:
    return i
    
  elif i is None: 
    return"no value"
    
  elif type( i)==int:
    if i < 100:
      return"less than 100"
    elif i ==100:
      return"equal to 100"
    else:
      return"more than 100"
      
  elif type(i) == list:
    if len(i)>=3:
      return i[2]
  else:
    return None
  