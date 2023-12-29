import re

def tokenize(y):
    tokens = []

   
    for x in y:
        
        if x in ['str', 'int', 'bool']:
            tokens.append(['DATATYPE', x])
        
        
        elif re.match("[a-z]", x) or re.match("[A-Z]", x):
            tokens.append(['IDENTIFIER', x])
        
       
        elif x in '*-/+%=':
            tokens.append(['OPERATOR', x])
        
        
        elif re.match(".[0-9]", x):
            if x[len(x) - 1] == ';':
                tokens.append(["INTEGER", x[:-1]])
                tokens.append(['END_STATEMENT', ';'])
            else:
                tokens.append(["INTEGER", x])

    return tokens


a = input("Enter your String :  ")
y = a.split()

result = tokenize(y)
print(result)

