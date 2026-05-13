from collections import Counter

# loop through each number in the list
def find_it(seq):

    # count how many times each number appears
    count  = Counter(seq)

    # loop through each number and  its frequency
    for num, freq in count.items():

        # check if the frequency is odd
        if freq % 2 != 0:
            return num
          
print(find_it([1, 1, 2])) # >>> 2
