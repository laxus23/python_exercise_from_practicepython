def fibonacci():
    game = 1
    while game == 1:
        number_of_elements = int(input('Provide a number of elements of fibonacci (must be >0), which you see on the '
                                       'screen: '))
        if number_of_elements > 0:
            list_to_convert = []
            for x in range(3):
                if len(list_to_convert) < 1:
                    list_to_convert.append(1)
            for x in list_to_convert:
                if len(list_to_convert) < number_of_elements - 1:
                    list_to_convert.append(x + list_to_convert[list_to_convert.index(x) - 1])
            x = [1]
            if number_of_elements == 1:
                print(list_to_convert)
            else:
                list_to_convert = x + list_to_convert
                print(list_to_convert)
        elif number_of_elements < 0:
            print('Sorry, you write a wrong number of elements.')
        try:
            game = int(input('Do u wanna provide a number again? Press 1 if yes\n'))
        except:
            print('You must provide only integer >0')


fibonacci()
