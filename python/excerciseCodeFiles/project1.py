#print all even and odd numbers between 0 to 50

print('The even numbers between 1 & 50 are given below\n')
for even in range(1,50):
    if(even%2 == 0):
        print(even)

print('\nThe odd numbers between 1 & 50 are given below\n')
for odd in range(1,50):
    if(odd%2 != 0):
        print(odd)