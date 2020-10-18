# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.
inp = input('Enter your age: ')
if inp >= 18:
    print('You are old enough to drive.')
else:
    print('You need 3 more years to learn to drive.')

# The following list contains some fruits:
# fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
inp = input('whats your desired fruit?')
if inp in fruits:
    print('That fruit already exist')
else:
    fruits.append(inp)
    print(inp)

# Here we have a person dictionary. Feel free to modify it!
    person = {
        'first_name': 'Asabeneh',
        'last_name': 'Yetayeh',
        'age': 250,
        'country': 'Finland',
        'is_marred': True,
        'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address': {
            'street': 'Space street',
            'zipcode': '02210'
        }
    }

# * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person and person['skills'] == ['']:
    print('this guy does not have skill')
else:
    print(person['skills'])
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person and person['skills'] == ['Python']:
    print('this guy can speak python')
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
elif 'skills' in person and person['skills'] == ['React', 'Javascript']:
    print('He is a front end developer')
elif 'skills' in person and person['skills'] == ['Node', 'Python', 'MongoDB', ]:
    print('he is a back end developer')
elif 'skills' in person and person['skills'] == ['Node', 'React', 'MongoDB', ]:
    print('he is a fullstacker')
else:
    print('unknown title')
