import random, string
def add(*nums):
     print(sum(nums))
    
def sub(*nums):
    print(nums - nums)

def multiply(*nums):
    print(multiply(nums))
    
    
def divide(*nums):
    print(nums // nums)
    
def reverse(*str):
    print(str.reversed())
    
def mangle(*str):
    print(str.reversed().upper())
    
def CallComplex(*func):
    Call = open("FILE NAME HERE", "r")
    if Call.endswith("()"):
        Call
        ##may not work##

def Debug():
    keywords = ["False", "async", "True", "for", "import", "else", "if", "elif", "not", "nonlocal", "while", "try", "lambda", "def", "del", "not", "in", "return", "continue", "class", "from", "global", "or", "raise", "finally", "yield", "is", "break", "except" ]
    FalseC = "Expected :"
    TrueC = "Expected :"
    forC = "Expected expression"
    importC = "Missing imports"
    elseC = "Expected :"
    ifC = "Expected expression"
    elifC = "Expected expression"
    de = open("General.py", "r")
    for word in keywords:
        print(f"Debugging {word}")
        #Absolutely minging
        if word not in FalseC:
            print(f"The debug has complete with errors: the error was: {FalseC}")
        faulty = keywords
    else:
        print("The debug has completed with errors. The errors were:")


def Hash():
    hash1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    hash2 = "abcdefghijklmnopqrstuvwxyz"
    hash3 = "!£$%^&*()_+"
    hash4 = "1234567890"
    hash5 = 300
    hash6 = hash1 +  hash2 + hash3 + hash4
    hash7 = ''
    for i in range(hash5):
     hash6 += ''.join(random.choice(hash6))

    print("Your special hash is:", hash7)
Hash()
    
    
    
    
