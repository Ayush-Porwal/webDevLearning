try:
    age = int(input('Enter your age-> '));
except ValueError:
    print('ERROR-> Age must be a number')
try:
    name = input('Enter your name-> ');
    if(type(int(name)) == int):
        print('ERROR-> Name cannot be an integer');
        exit();
except :
    pass;
