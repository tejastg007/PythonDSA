# basic string methods
name = "tony stark"
print('slice->', name[0:4])
print('slice->', name[4:10])
print('slice->', name[1:])
print('slice->', name[:4])
print('slice->', name[5:-1])
print('slice->', name[-5:])
print('slice->', name[:-1])
print('capitalize-> ', name.capitalize())
print('uppercase ', name.upper())
print('lowercase ', name.lower())
print('isUpper ', name.isupper())
print('isLower ', name.islower())
print('count->', name.count('t'))  # counts the appearance of given parameter

name = " tony stark "
print('length ', len(name))
print('strip ', len(name.strip()))  # removes leading and trailing spaces
# variants- lstrip, rstrip

splitExample = "i am the string"
print('split-> ', splitExample.split())  # converts string into list
print('split-> ', splitExample.split(' ', 2))
print('split-> ', splitExample.rsplit(' ', 2))

name = "Code in Python"
print('replace ', name.lower().replace("python", "java"))

numString = '123'
alphaString = 'abc'
alphaNum = 'abc123'
noAlphaNum = 'abc-123'
print('isAlpha ', numString.isalpha())
print('isAlpha ', alphaString.isalpha())
print('isNum ', numString.isnumeric())
print('isNum ', alphaString.isnumeric())
print('isalnum ', alphaNum.isalnum())
print('isalnum ', noAlphaNum.isalnum())


print('find ', name.find('o'))  # finds least index of occurance

# finds least index of occurance after start parameter
print('find ', name.find('o', 5))

# find highest index of occurance after start parameter
print('find ', name.rfind('o'))

partitionExample = 'i am the python programmer'
print('partition ', partitionExample.partition(' '))  # returns tuble of 3

print('center', name.center(20, '-'))
print('ljust', name.ljust(20, '-'))
print('rjust', name.rjust(20, '-'))


formatString = 'format string {name}'  # only parameter can be passed
print('format->', formatString.format(name='name'))


fString = f'fString {name}'  # can use the variable directlu
print('fstring', fString)

swapCase = 'SwapCaSE'
print('swapcase->', swapCase.swapcase())

num = 1234
print('zfill->', str(num).zfill(6))
