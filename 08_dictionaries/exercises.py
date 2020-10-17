# Create an empty dictionary called dog
dog = {}
# Add name, color, breed, legs, age to the dog dictionary
dog = {'type': 'anjing', 'color': 'red'}
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {'first_name': 'otonashi', 'last_name': 'han', 'gender': 'male', 'age': 19, 'marital status': 'unmarried', 'skills': [
    'procrastinating', 'binge eater', 'sleeping enthusiast'], 'country': 'Indonesia', 'city': 'Jember', 'address': 'on Gods earth'}
# Get the length of the student dictionary
len(student)
# Get the value of skills and check the data type, it should be a list
print(type(student['skills']))
# Modify the skills values by adding one or two skills
student['skills'].append('fast runner')
print(student['skills'])
# Get the dictionary keys as a list
print(student.keys())
# Get the dictionary values as a list
print(student.values())
# Delete one of the items in the dictionary
student.pop('address')
print(student)
# Delete one of the dictionaries
del dog
