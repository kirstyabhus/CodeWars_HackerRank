# https://www.codewars.com/kata/5679aa472b8f57fb8c000047/python

def find_even_index(arr):
    # current index
    index = 0
    # sum of values to the left of index
    totalLeft = 0
    # sum of values to the right of index
    totalRight = 0
    # last value index
    lastIndex = len(arr) - 1

    # loop through integers of list
    while True:
        # when at the first index
        if index == 0:
            # total of right side of index
            totalRight = sum(arr[1:])

            # if index is 0, totalLeft will be  (there are no values left of start)
            # if the sums are equal return the position of the index (0)
            if totalLeft == totalRight:
                return 0
            # if not, move onto next index
            else:
                index += 1
                continue

        # when at the last index
        if index == lastIndex:
            # find total of left side of index
            totalRight = 0
            totalLeft = sum(arr[:lastIndex])
            # if at last index, totalRight will be 0 (there are no values right of last index)
            if totalLeft == totalRight:
                return lastIndex
            # if we've reached the last index and there has been no even sum, then there is
            # no position in the array that meets the requirements
            else:
                return -1

        # for any other index other than start or last
        # find total or left side and total of right side
        totalLeft = sum(arr[:index])
        totalRight = sum(arr[index + 1:])

        # if the totals are equal return this index
        if totalLeft == totalRight:
            return index

        # go to next index
        index += 1

# BETTER
#def test(arr):
#    for i in range(len(arr)):
#        if sum(arr[:i]) == sum(arr[i + 1:]):
#            return i
#    return -1
# print(test([10,-80,10,10,15,35,20]))

print(find_even_index([10,-80,10,10,15,35,20]))