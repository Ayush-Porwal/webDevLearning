def add(a,b):
    return a+b;
def subtract(a,b):
    return a-b;
def multiply(a,b):
    return a*b;
def divide(a,b):
    return a/b;

num = [0 , 0];
choice = input('Choose an option\n1 : Add\n2 : Subtract\n3 : Multiply\n4 : Divide\n-> ');

option = 'y';
while(option == 'y' or option == 'Y'):
    if(int(choice) == 1):
        print('You chose addition');
        for var in range(0,2):
            num[var] = input('Enter the number ' + str(var + 1) + '-> ');
        print('The result is:- ', add(int(num[0]),int(num[1])));
    elif(int(choice) == 2):
        print('You chose subtraction');
        for var in range(0,2):
            num[var] = input('Enter the number ' + str(var + 1) + '-> ');
        print('The result is:- ', subtract(int(num[0]),int(num[1])));
    elif(int(choice) == 3):
        print('You chose multiplication');
        for var in range(0,2):
            num[var] = input('Enter the number ' + str(var + 1) + '-> ');
        print('The result is:- ', multiply(int(num[0]),int(num[1])));
    elif(int(choice) == 4):
        print('You chose division');
        for var in range(0,2):
            num[var] = input('Enter the number ' + str(var + 1) + '-> ');
        print('The result is:- ', divide(int(num[0]),int(num[1])));
    else:
        print('Invalid Choice! ~ --Exiting Program--');
        break;
    option = input('Do you want to continue?(y/n)-> ');
    if(option == 'y' or option == 'Y'):
        choice = input('Choose an option\n1 : Add\n2 : Subtract\n3 : Multiply\n4 : Divide\n-> ');
