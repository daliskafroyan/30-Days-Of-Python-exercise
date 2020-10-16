# Find the length of your list
print(len(['ichi', 'ni', 'san']))

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon', 'kaneki']

# Print the first, middle and last company
print('{}, {}, {}'.format(it_companies[0], it_companies[int(
    len(it_companies)/2)], it_companies[len(it_companies)-1]))

# Print the list after modifying one of the companies
it_companies[5] = 'Netflix'
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
print(it_companies[5].upper())

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = front_end.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
china, russia, usa, *scandic = ['China', 'Russia',
                                'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print('{}, {}, {}, {}'.format(china, russia, usa, scandic))

# The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
# Add the min age and the max age again to the list
# Find the median age (one middle item or two middle items divided by two)
# Find the average age (sum of all items divided by their number )
# Find the range of the ages (max minus min)
# Compare the value of (min - average) and (max - average), use abs() method
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
ages.append(ages[0])
ages.append(ages[len(ages)-1])
ages.sort()

median = 0
if len(ages) % 2 == 0:
    if_even_var_1 = ages[int((len(ages)/2-2))]
    if_even_var_2 = ages[int((len(ages)/2-1))]
    median = (if_even_var_1+if_even_var_2)/2
else:
    median = ages[(int(len(ages)/2))]
print(median)
