#space is x which is then timsed by the amount fo spaces you want, this instance its 1
x=' ';
#print
print('My'+1*x+'Shopping'+1*x+'List')
#shopping list with items needed
My_Shopping_List= ['pasta','salad','yogurt','sweets','crisps']
print(My_Shopping_List)
#adding chocolate to my list
My_Shopping_List.append('chocolate')
print(My_Shopping_List)
#listing strings
print(My_Shopping_List[0])
print(My_Shopping_List[1])
print(My_Shopping_List[2])
print(My_Shopping_List[3])
print(My_Shopping_List[4])
print(My_Shopping_List[5])
#changing something in the list, this instance changing 3 sweets is now cherries
My_Shopping_List[3] = 'cherries'
#creating a loop for my shopping list so it will print whole list instead of writting it all out again
for item in My_Shopping_List:
  print(item)
#creating an infinate loop for user input
result=input('\n Add an item')
print(result)
#creating a statement for the user input so that when user input is finished the loops ends.
while True:
  item=input('\nitem (leave blank to exit); ')
#the below action looks for an empty string to end the input
  if not item:
    break
  else:
    My_Shopping_List.append(item)
for item in My_Shopping_List:
    print(item)

