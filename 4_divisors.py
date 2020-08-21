def number_of_divisors(input_number: int):
    """
    Exercise 4
     Create a program that asks the user for a number and then prints out a list of all the
    divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another
    number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
    """
    # input_number = int(input("Provide a number and the u see all of divisors of that number: "))
    x = 1
    list_of_divisors = []
    while x <= input_number:
        if input_number % x == 0:
            list_of_divisors.append(x)
        x += 1
    print(f'Below divisors list of {input_number} number:\n{list_of_divisors}')


number_of_divisors(input_number=533)
