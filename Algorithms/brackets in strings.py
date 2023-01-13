
# Close bracket search function.

str1 = 'What are you thinking? (about it)'
str2 = 'There are many vegetables (and fruits.'
str3 = 'Hello!'

def is_brackets(str):
    if '(' in str:
        index = str.find('(')
        if ')' in str[index:]:
            return 'Brackets are closed'
        else:
            return 'Brackets are not closed'
    return 'There are no brackets'

print(is_brackets(str1))    # Brackets are closed
print(is_brackets(str2))    # Brackets are not closed
print(is_brackets(str3))    # There are no brackets