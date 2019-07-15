print('\n## STRINGS')
message = 'my message'
print(message)

print('\n### multiline string')
multiline_message = '''my multiline
message'''
print(message)

print('\n### indexes of string')
print(len(message))
print(message[1])
print(message[1:4])
print(message[:4])
print(message[4:])

print('\n### methods of string')
print(message.lower())
print(message.upper())
print(message.count('message'))
print(message.find('message'))
new_message = message.replace('message','world').replace('my','hello') ## replacing parts of a string
message = message.replace('message','name is M4R10') ## replacing parts of a string

print( '\n### string concatenation' )
print(message + ' ' + new_message) ## oldest methods
print( '{} {}'.format(message,new_message) ) ## string formatting (e.g. fprint)

print('\n\t#### fstrings')
print(f'\t{message} {new_message}') ## available since python 3

print('\n### information about objects')
print('''
    print(dir(message))
    print(help(str))
    print(help(str.lower))
''')

