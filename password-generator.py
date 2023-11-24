import random

# Character sets
lettersLowerCase = 'abcdefghijklmnopqrstuvwxyz'
lettersUpperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '`~!@#$%^&*()-_=+[{]}\|;:\'",<.>/?'

# Flags for each type of character
isUsingLettersLowerCase: bool = False
isUsingLettersUpperCase: bool = False
isUsingNumber: bool = False
isUsingSymbolsNumber: bool = False

# Maximum length of the password
maxPasswordLength: int = 20

# Use generateCustomPassword or generateAutoPassword
isGenerateAutoPassword: bool = False

def returnRandomIndex(maxLength: int): 
    return random.randint(0, maxLength - 1)

def generateCustomPassword():
    if isUsingLettersLowerCase == False & isUsingLettersUpperCase == False & isUsingNumber == False & isUsingSymbolsNumber == False:
        print('All custom password options can not be false.')
        exit()

    availableCharacters = ''
    
    if isUsingLettersLowerCase:
        availableCharacters += lettersLowerCase
    if isUsingLettersUpperCase:
        availableCharacters += lettersUpperCase
    if isUsingNumber:
        availableCharacters += numbers
    if isUsingSymbolsNumber:
        availableCharacters += symbols

    password = ''
    for _ in range(maxPasswordLength):
        password += availableCharacters[returnRandomIndex(len(availableCharacters))]

    return password

def generateAutoPassword():
    availableCharacters = lettersLowerCase + lettersUpperCase + numbers + symbols

    password = ''
    for _ in range(maxPasswordLength):
        password += availableCharacters[returnRandomIndex(len(availableCharacters))]

    return password

def getInput(prompt, default):
    response = input(prompt)
    return response if response else default

# Generate auto password or generate password with custom options
isGenerateAutoPassword = getInput('Auto generate password? If "yes" type 1, if not type 0: ', '0') == '1'

if isGenerateAutoPassword:
    print('Generated Password:', generateAutoPassword())
    exit()

# Inputs for each type of character with default values
isUsingLettersLowerCase = getInput('Will lowercase letters be used? If "yes" type 1, if "no" type 0: ', '0') == '1'
isUsingLettersUpperCase = getInput('Will uppercase letters be used? If "yes" type 1, if "no" type 0: ', '0') == '1'
isUsingNumber = getInput('Will numbers be used? If "yes" type 1, if "no" type 0: ', '0') == '1'
isUsingSymbolsNumber = getInput('Will special characters be used? If "yes" type 1, if "no" type 0: ', '0') == '1'

maxPasswordLengthInput = getInput('Enter the maximum length of the password: ', '20')
maxPasswordLength = int(maxPasswordLengthInput)

# Generate and print the password
print('Generated Password:', generateCustomPassword())
