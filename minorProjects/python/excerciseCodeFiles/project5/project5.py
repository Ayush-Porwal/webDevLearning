from module import checkEven_Or_Odd;

val = input('Enter the number-> ');
try:
    checkEven_Or_Odd(int(val));
except ValueError:
    print('ERROR-> Failed to convert your input into an integer');
