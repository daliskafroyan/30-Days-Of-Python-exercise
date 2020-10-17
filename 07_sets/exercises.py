# sets
it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
print(len(it_companies))
# Add 'Twitter' to it_companies
it_companies.add('twitter')
# Insert multiple IT companies at once to the set it_companies
it_companies.update(['LINE', 'NETFLIX', 'Intel'])
# Remove one of the companies from the set it_companies
it_companies.remove('LINE')
# Join A and B
A.update(B)
# Find A intersection B
A.intersection(B)
# Is A subset of B
A.issubset(B)
# Delete the sets completely
del it_companies
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
set(age)
# Explain the difference between the following data types: string, list, tuple and set
print('string = sequence of characters and immutable')
print('list = in another languages are also called array, mutable and heterogenous')
print('tuples = sequence of immutable objects, just like list but immutable and a bit faster')
print('sets = every member is unique and mutable')
# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? You did not learn loops yet you can do it manually.
print(len(set('I am a teacher and I love to inspire and teach people')))
