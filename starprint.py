
print("Input q/e for quit/exit \n")

quit = False

while quit is False:
    n = input("How many times do you want to print star pattern:")

    if n == "q" or n== "e":
        quit = True
    else:
        print("\n -------- Star Pattern Code --------\n ")

        order = int(input("1 for increasing order and 0 for decreasing order:"))
        number = int(n)

        def converter(pattern):
            if pattern == 1:
                return True
            elif pattern == 0:
                return False

        if number< 0:
            print("You have input negative number")

        else:
            if order == 0 or order == 1:

                if (converter(order)):
                    print("\n -------- pattern in increasing order --------")

                    for v in range(number+ 1):
                        print("*" * v)

                elif (not converter(order)):
                    print("-------- pattern in decreasing order --------")

                    for v in range(number,0,-1):
                        print("*"*v)
                    # or we can do with while loop like

                    # while number >= 1:
                    #     print("*" * number)
                    #     number = number - 1
            else:
                print("You can to only input 0 or 1!")