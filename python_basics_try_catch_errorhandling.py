#!/usr/bin/python3

try:
    if "wrong word" != "word":
        raise SyntaxError('Wrong word used Exception')
except Exception as E:
    print(E)
else:
    pass
finally:
    print( "But this is run anyways" )

print()

try:
    if "word" != "word":
        raise SyntaxError('Wrong word used Exception')
except Exception as E:
    print(E)
else:
    print("The right word was used")
finally:
    print( "But this is run anyways" )