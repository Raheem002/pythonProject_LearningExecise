pi = 12
print(pi)
print(type(pi))

i = 12
i2 = 34
result = i / i2
print(type(result))

# RAW string r - it will take as it is nothing will change in the results response

a = r'C:\dir12\game_you'
print(a)

# Formatting string f - it will replace the value of the variable
# {} - Placeholders

first_name = 'Harry'
last_name = 'potter'
print(first_name + ' ' + last_name)
print(first_name, last_name)

print(f'your full name is {first_name} + {last_name}')

a = 12
num = 280
print(f'the final number is {num * 3}')

num = 3
print(f'{num}X1={num}')
print(f'{num}X2={num * 2}')
print(f'{num}X3={num * 3}')

b = 2
print(f"{b}X1={b}")
print("{}X2={},{}".format(b, b*2, 6))
