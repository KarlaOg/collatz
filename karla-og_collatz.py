def collatz():
    maxNum = 0 
    realNum = 0
    while True:
        realNum += 1
        number = realNum
        counter = 1
        while number != 1:
            if number % 2 == 0:
                number = int(number / 2)
                counter += 1
            else:
                number = int(3 * number + 1)
                counter += 1

        if  maxNum < counter:
            maxNum = counter
            print("Collatz from " + str(realNum) + " of len " + str(counter))
collatz()