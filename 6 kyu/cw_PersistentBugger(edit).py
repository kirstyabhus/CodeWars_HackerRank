# turn the number into a string
# split the numbers' digits into a list

# if the number already has a length of 1
# just return 0

# while length of the number is not 1
# for loop through each digit of the number
# new number is product of all the digits in old number (digits are converted into int)
# find the length of the new number (which had now been converted to string)
# take count of how many times the while loop is running

# once length of number is finally 1
# return how many times the while loop ran


def persistence(n):
    # convert the number to str, then split it by its digits into a list
    nList = list(str(n))
    # initialise the total (which is the product of each digit)
    total = 1
    # find the length of the initial number
    lengthNum = len(nList)
    # tracker for while loop repeats
    # i.e number of times you must multiply the digits in num until you reach a single digit.
    count = 0

    # if the length of the num is already 1 then just return 0
    if lengthNum == 1:
        return 0

    # if length is not 1
    while lengthNum != 1:
        # loop through each digit of the number
        for num in nList:
            # find the product of the digits
            total *= int(num)

        # separate each digit on the new number into a list
        nList = list(str(total))
        # find the length of the new number
        lengthNum = len(nList)
        # re-initialise total to 1 for the next round
        total = 1
        # keep count of how many rounds are occurring
        count += 1

    return count
