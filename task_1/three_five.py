def three_five(start: int = 1, stop: int = 100) -> None:
    """
    Prints the numbers from 1 to 100 as default or a user-defined range.
    For multiples of three, prints “Three” instead of the number. For multiples of five, prints “Five”.
    For numbers which are multiples of both three and five, prints “ThreeFive”.

    :param start:int - Lower bound (inclusive) for printing range. Default = 1.
    :param stop: int - Upper bound (inclusive) for printing range. Default = 100.

    :return: int | str - print output of three_five implementation
    """
    for i in range(start, stop + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('ThreeFive')

        elif i % 3 == 0:
            print('Three')

        elif i % 5 == 0:
            print('Five')

        else:
            print(i)


three_five()
