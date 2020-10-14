# Check the data type of all your variables using type() built-in function
print(type(['list']))
print(type('list'))
print(type({'list'}))
print(type((1, 2)))

# Using the len() built-in function find the length of your first name
print(len('daliska'))

# Compare the length of your first name and your last name
print(len('royan'))

# Declare 5 as num_one and 4 as num_two
# Add num_one and num_two and assign the value to a variable _total
# Subtract num_two from num_one and assign the value to a variable _diff
# Multiply num_two and num_one and assign the value to a variable _product
# Divide num_one by num_two and assign the value to a variable _division
# Use modulus division to find num_two divided by num_one and assign the value to a variable _remainder
# Calculate num_one to the power of num_two and assign the value to a variable _exp
# Find floor division of num_one by num_two and assign the value to a variable _floor_division

num_one = 5
num_two = 4

var_total = num_one + num_two
var_diff = num_two - num_two
var_product = num_two * num_one
var_division = num_two / num_one
var_remainder = num_two % num_one
var_exp = num_one ^ num_two
var_floor_division = num_one//num_two

print(var_total, var_diff, var_product, var_division,
      var_remainder, var_exp, var_floor_division)

# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable area_of_circle
# Calculate the circumference of a circle and assign the value to a variable circum_of_circle
# Take radius as user input and calculate the area.

area_of_circle = 3.14*(30 ^ 2)
circum_of_circle = 3.14*(30*2)
print(area_of_circle, circum_of_circle)

radius = input('circle radius: ')
area_of_circle_inp = 3.14*(radius ^ 2)
circum_of_circle_inp = 3.14*(radius*2)
print(area_of_circle_inp, circum_of_circle_inp)
