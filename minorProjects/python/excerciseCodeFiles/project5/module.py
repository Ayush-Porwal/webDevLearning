def checkEven_Or_Odd(num):
    try:
        if(type(num) == int):
            if(num%2 == 0):
                return print('is Even');
            else:
                return print('is Odd');
        else:
            raise Exception('ERROR-> Not an integer');
    except Exception as error:
        print(error);
