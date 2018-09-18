age = -1
while age <= 0:
    try:
        age = int(input('Please Enter Your Age: '))
        if age <= 0:
            print('Your age must be positive')
    except:
        print('Invalid response!')
