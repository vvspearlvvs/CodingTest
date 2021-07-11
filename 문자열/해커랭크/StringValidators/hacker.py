def isalnum(string):
    for s in string:
        if s.isalnum():
            return True
    return False

def isalpha(string):
    for s in string:
        if s.isalpha():
            return True
    return False

def isdigit(string):
    for s in string:
        if s.isdigit():
            return True
    return False

def islower(string):
    for s in string:
        if s.islower():
            return True
    return False

def isupper(string):
    for s in string:
        if s.isupper():
            return True
    return False


s=input()
print(isalnum(s))
print(isalpha(s))
print(isdigit(s))
print(islower(s))
print(isupper(s))

print(s.isalnum())
