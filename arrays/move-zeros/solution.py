def move_zeros(lst):
    # list where non-zero values will be stored
    result = []

    # loop through each element in the list
    for n in lst:

        # add only values that are not zero
        # "or n is False" prevents False from being moved,
        # since False == 0 in Python
        if n != 0 or n is False:
            result.append(n)

    # create a list containing the same number of zeros found
    zeros = [0] * lst.count(0)

    # add the zeros to the end of the list
    result.extend(zeros)

    # return the final list
    return result

print(move_zeros([1, 5, 9, 0, 8, 3, 0]))
