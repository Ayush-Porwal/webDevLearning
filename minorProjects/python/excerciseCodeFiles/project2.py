#Read inputs from user:- name & age. Store them in a file. Read & display the file content on console screen.

fileName = 'personalData.txt'
WRITE = 'w'
READ = 'r'

name = input('Enter your name:- ')
age = input('Enter your age: ')

myFile = open(fileName , mode = WRITE)
myFile.write(name + ', ' + age)
print('Data saved to file\n')

myFile.close()

myFile = open(fileName , mode=READ)
print('The content of file is displayed below\n')
print(myFile.read())

myFile.close()