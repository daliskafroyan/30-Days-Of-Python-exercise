# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print('Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python')


# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print('{} {} {}'.format('Coding', 'For', 'All'))


# Cut(slice) out the first word of Coding For All string.
string = 'Coding for All'
list_word = []
for i in string:
    list_word.append(i)
    if i == ' ':
        break

print(''.join(list_word))


# Check if Coding For All string contains a word Coding using the method index, find or other methods.
string_2 = 'Coding for All'


def find_string(string):
    if string.find('Coding') == -1:
        return False
    else:
        return True


print(find_string(string_2))


# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
string_3 = '   Coding For All      '
print(string_3.strip(' '))


# Use a tab escape sequence to write the following lines.
# Name      Age     Country
# Asabeneh  250     Finland
print('Name\t\tAge\t\tCountry\nAsabeneh\t250\t\tFinland')
