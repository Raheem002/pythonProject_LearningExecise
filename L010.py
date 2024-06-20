# OPERATORS
# ----------

# Operators are used to perform operations by using operands

# there are three types of operator depending on the number of operands required.
# 1.Binary Operator (2 operands are required)
# 2.Unary Operator (Only one operand is required)


# Assignment Operator
# Single Operator "=" - Nothing but it will assign the value to right to left
# Example - Name = 'Operator'

# Double Operator "==" - Compare Operator (Boolean)

# fun = {1, 2, 7, 9 , 9 , 9 ,4, 8, 8}
# print(fun)
# fun.add(10)
# print(fun)
# fun.remove(1)
# print(fun)


# x = (1 == True)
# y = (2 == False)
# a = True + 4
# b = False + 1
# print(type(a))


AGE = +78  # This is Called Unary Operator (here Pycharm remove the + because this is self explanatory)
print(AGE)
num = -3
print(AGE + num)

#NOT Operator (They only work with Boolean)
my_marriage = True
print(not my_marriage)

# is Operator - identity operator (Return the response in Boolean)

a = 12
b = 4
c = True
print(a is b) #True
print(a is not b) #False

my_list1 = [1, 2, 3]
my_list2 = [1, 2, 3]
print(my_list1 is my_list2) # False - Why becasue the items are store in  different continer
