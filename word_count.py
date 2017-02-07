def words(text):
  empt_dict = {}      #initialize an empty dictionary that we'll append our output
  lst = text.split()  #create a list from the string input
  
  #use a for loop to go through every item in the list
  #and compare it with other items on the list
  for x in lst:
    count = 0   #initialize count as zero
    for y in lst:
      if y == x:
        count += 1
        
    empt_dict[x] = count
  return empt_dict
  
  #*disclaimer: yet to figure out how to pass the integer test
