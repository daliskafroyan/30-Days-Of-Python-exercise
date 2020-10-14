

# Declare your age as integer variable
age = 21
# Declare your height as a float variable
height = 180.5
# Declare a complex number variable
complex = (1 + 10j)
# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = input('Enter base: ')
height = input('Enter height: ')
area = 0.5*base*height
print('The area of the triangle is ', area)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = input('Enter side a: ')
b = input('Enter side b: ')
c = input('Enter side c: ')
perimeter = a * b * c
print('The perimeter of the triangle is ', perimeter)

# Find the length of 'python' and 'jargon' and make a falsy comparison statement.
print(len('python') == len('jargon'))

# Use and operator to check if 'on' is found in both 'python' and 'jargon'
print(('on' in 'python') and ('on' in 'jargon'))

# Find the length of the text python and convert the value to float and convert it to string
print(str(float(len('python'))))

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = 8
print(True if number % 2 == 0 else False)

# The floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7//3 == int(2.7))

# Check if int('9.8') is equal to 10 (can't be converted to integer because it's a fraction)
print(int('9.8') == 10)


# Write a python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
for i in range(1, 6):
    print(i, i**0, i**1, i**2, i**3)
