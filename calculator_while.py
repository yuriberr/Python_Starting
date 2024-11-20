""" Calculator using while """
# Translated by myself so i'm sorry if made some mistakes #
while True:

    number_1 = (input('\nType a number:    '))
    if number_1.isdigit():  # Verifies if the number entered is an integer
        number_2 = (input('\nType another number: '))
        if number_2.isdigit():
            operator = input('\nType an operator for the calculation (+, -, *, /): ')
        
            ### CALCULES ###
            # Addition:
            if operator == '+':
                addition = int(number_1) + int(number_2)
                print(f'\n{number_1} + {number_2} = {addition}')
                print(f'The result of the addition is: {addition}')

            # Subtraction:
            elif operator == '-':
                subtraction = int(number_1) - int(number_2)
                print(f'\n{number_1} - {number_2} = {subtraction}')
                print(f'The result of the subtraction is: {subtraction}')

            # Multiplication:
            elif operator == '*':
                multiplication = int(number_1) * int(number_2)
                print(f'\n{number_1} X {number_2} = {multiplication}')
                print(f'The result of the multiplication is: {multiplication}')

            # Division:
            elif operator == '/':
                division = int(number_1) / int(number_2)
                print(f'\n{number_1} / {number_2} = {division}')
                print(f'The result of the division is: {division}')
            else:
                print('Invalid operator')
                
                
        else:
            print('This is not a number')
    else:
        print('This is not a number')
    logout = input('\nDo you want to leave? [y]es: ').lower().startswith('y')

    if logout is True:
        break
