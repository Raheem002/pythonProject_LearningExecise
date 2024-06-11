#List
shopping_list =['qw', 'er', 'ty', 'oi']
#add items
#remove items
#update items
#view items
#Exit

print(shopping_list)
print(len(shopping_list))
print(id(shopping_list))
print(shopping_list[0])
print(shopping_list[-1])

#test = [1, 'test', 3.99, True]
#print(type(test))

shopping_list.append('rr') #Add the item in the list
print(shopping_list)

shopping_list.insert(1, 'qq') #replacing the item by giving the index value and the object value
print(shopping_list)

shopping_list.extend(['hh','ll']) #Adding multiple items in the list
print(shopping_list)

print(len(shopping_list))

shopping_list.remove('ll') #Removing the item in the list
print(shopping_list)
print(shopping_list.pop()) #removing the last item in the list
print(shopping_list)
print(shopping_list.index('rr'))#shows the index of the item in the list
shopping_list.reverse()#it will reverse the items in the list
print(shopping_list)
shopping_list.sort()#it will show the items in the assending order
print(shopping_list)