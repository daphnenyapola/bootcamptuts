def words(word):
  word_list= word.split()
  my_dict={}
  for x in word_list:
    my_dict[x] =word_list.count(x)
  print(my_dict)
words("olly olly in come free")      