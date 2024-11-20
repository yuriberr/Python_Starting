""" Calculator using while """
# Translated by myself so i'm sorry if made some mistakes #
while True:
    number_1 = (input('\nType a number:    '))
    if number_1.isdigit():  # Verifies if the number entered is an integer
        number_2 = (input('\nType another number: '))
        if number_2.isdigit():
            operator = input(
                '\nType an operator for the calculation (+, -, *, /): ')
            if len(operator) > 1:
                print('Type only one operator.')
                continue
            ### CALCULES ###
            # Addition:
            if operator == '+':
                addition = int(number_1) + int(number_2)
                print(f'\n{number_1} + {number_2} = {addition}')
                print(f'\nThe result of the addition is: {addition}')
            # Subtraction:
            elif operator == '-':
                subtraction = int(number_1) - int(number_2)
                print(f'\n{number_1} - {number_2} = {subtraction}')
                print(f'\nThe result of the subtraction is: {subtraction}')
            # Multiplication:
            elif operator == '*':
                multiplication = int(number_1) * int(number_2)
                print(f'\n{number_1} X {number_2} = {multiplication}')
                print(f'\nThe result of the multiplication is: {
                      multiplication}')
            # Division:
            elif operator == '/':
                division = int(number_1) / int(number_2)
                print(f'\n{number_1} / {number_2} = {division}')
                print(f'\nThe result of the division is: {division}')
            else:  # Verifies if the operator entered is valid
                print('Invalid operator')
        else:  # Verifies if the second number entered is an integer
            print('This is not a number')
    else:  # Verifies if the first number entered is an integer
        print('This is not a number')
    logout = input('\nDo you want to leave? [y]es or [n]o: ').lower().startswith('y')  # Verifies if the user wants to stop calculating
    if logout is True:
        print('\nGoodbye!')
        break
