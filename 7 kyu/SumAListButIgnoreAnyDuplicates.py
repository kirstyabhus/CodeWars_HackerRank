# https://www.codewars.com/kata/5993fb6c4f5d9f770c0000f2/python

def sum_no_duplicates(l):
    # sum of single integers
    singleSum = 0

    # iterate through integers of the list
    for num in l:
        # if only single copy of number
        if l.count(num) == 1:
            # add it to single copy total
            singleSum += num

    return singleSum
