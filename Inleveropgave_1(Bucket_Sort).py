import time
import math
import random


def getbetterlist(simplelist):
    """
    This function makes every simplelist a list with all the elements the same length as the longest element
    e.g.: [123.45, 78] gives [123.45, 078.00]
    :param simplelist:
    :return: list containing elements with same length
    """
    def getdecimallist(lst):
        """
        :param lst:
        :return: list containing elements with same length behind (decimals)
        e.g.: [23.45, 78] gives [23.45, 78.00]
        """
        mostdecimalplaces = 0  # saves
        for num in lst:
            num = str(num)
            if '.' in num:
                if mostdecimalplaces < len(num.split('.')[1]):
                    mostdecimalplaces = len(num.split('.')[1])
        decimallist = [str(format(float(num), '.{}f'.format(mostdecimalplaces))) for num in lst]
        return decimallist

    def gethighzerolist(lst):
        """
        :param lst:
        :return: list containing elements with same length in front (hundreds/thousands)
        e.g.: [123, 78] gives [123, 078]
        """
        rounded_list = [round(abs(num)) for num in simplelist]
        mostnaturalnumbers = math.ceil(math.log(max(rounded_list), 10))
        highzeroslist = []
        for num in lst:
            num = str(num)
            bits = num.split('.')
            if '-' in num:
                highzeroslist.append("%s.%s" % (bits[0].zfill(mostnaturalnumbers + 1), bits[1]))
            else:
                highzeroslist.append("%s.%s" % (bits[0].zfill(mostnaturalnumbers), bits[1]))
        #         print(highzeroslist)
        return highzeroslist

    decimallist = getdecimallist(simplelist)
    betterlist = gethighzerolist(decimallist)
    return betterlist

def positiv_negative_split(lst):
    """
    :param list containing negatives and positives:
    :return: 2 lists containing only negatives or positives
    e.g: [-1, 2, 3, -4] gives [2, 3] & [-1, -4]
    """
    negative_betterlist = [y for y in lst if float(y) < 0]
    positive_betterlist = [x for x in lst if float(x) > 0]
    return negative_betterlist, positive_betterlist

def Ihasabucket(betterlist, negative):
    """
    This Function uses the list (containing elements with the same length) to get the length of the elements (default is the first of the list)
    and used that value to reverse loop through every element in the list. This value (0-9) will be set in a bucket of that indexnumber
    e.g. 153 goes to the fourth(3+1) bucket and 527 goes to the eight(7+1) bucket. After that the buckets will be empty in the list and this
    will loop until every character has been collected in buckets (except the . and the minus). Eventually the elements with the highest value
    at the last element which is higher than 0, get prioritized in the buckets and will be empty later in the list.
    e.g. [123, 99], first 3 vs 9 which 9 gets last, then 2 vs 9 which 9 gets last, but then 1 vs *empty* aka 0 and then the 1 wins which means
    123 will be set at last of the list. This bucket will be reversed when negative is True, so the last become first and the first becomes last.
    :param betterlist:
    :return: a sorted list
    """
    for character in range(len(betterlist[0])):
        buckets = [[], [], [], [], [], [], [], [], [], []] #(re)creates 10 empty buckets
        for index in range(len(betterlist)):
            try:
                buckets[int(betterlist[index][(len(betterlist[0]) - character) - 1])].append(betterlist[index]) #adds the number of the index it is at, and adds it to the bucket
            except ValueError: #against the "-" value and the "." value
                continue

        if buckets != [[], [], [], [], [], [], [], [], [], []]: #catching empty buckets, if the values not got filled (like the valuerror)
            if negative:
                buckets.reverse() #if indicated that it's a negative list, reverse the buckets
            betterlist  = [y for x in buckets for y in x]
    return betterlist


def runthemainprogram(lst):
    """
    This function is the main function to combine the early coded functions. It will first run the betterlist function to create zero's on both
    the front and the end of most elements if they are not long enough compared to the longest element.
    After that the function will check if the input list is negative. If so the list will
    be split and the list will both be sorted separately. If not the list will be sorted as a whole. At the end the elements will be set to
    floats to make sure they are at there original state.
    :param lst:
    :return: sorted list
    """
    start = time.time()
    print("Using  getbetterlist function on simple list...")
    betterlist = getbetterlist(lst)
    print("Done!")
    if any(float(n) < 0 for n in betterlist): #are there negatives in the list?
        print("Contains negatives")
        print("Splits values...")
        negative_betterlist, positive_betterlist = positiv_negative_split(betterlist)
        print("Done!" + ' Took: ' + str(time.time() - start) + ' seconds')

        print("Uses Bucket Sort on positive better list...")
        sorted_positive_list = Ihasabucket(positive_betterlist, False)
        rounded_sorted_positive_list = [float(num) for num in sorted_positive_list]
        print("Done!" + ' Took: ' + str(time.time() - start) + ' seconds')

        print("Uses Bucket Sort on negative better list...")
        sorted_negative_list = Ihasabucket(negative_betterlist, True)
        rounded_negative_positive_list = [float(num) for num in sorted_negative_list]
        print("Done!" + ' Took: ' + str(time.time() - start) + ' seconds')

        print("Adding Together...")
        sortedlist = rounded_negative_positive_list + rounded_sorted_positive_list
        print("Done!" + ' Took: ' + str(time.time() - start) + ' seconds')
    else:
        print("Contains non negatives")
        print("Uses Bucket Sort on better list...")
        notrounded_sortedlist = Ihasabucket(betterlist, False)
        sortedlist = [float(num) for num in notrounded_sortedlist]

        print("Done! ")
    print('Sorting a list with ' + str(len(lst)) + ' length took: ' + str(time.time() - start) + ' seconds\n')
    return sortedlist

def randomlistgenerator():
    """
    :return: 3 random generated lists
    """
    randomlist1 = []
    randomlist10 = []
    randomlist30 = []
    for i in range(0, 1000):
        n = random.uniform(-100, 100)
        randomlist1.append(n)

    for i in range(0, 10000):
        n = random.uniform(-100, 100)
        randomlist10.append(n)

    for i in range(0, 30000):
        n = random.uniform(-100, 100)
        randomlist30.append(n)
    return randomlist1, randomlist10, randomlist30


randomlist_thousand, randomlist_tenthousand, randomlist_thirtythousand = randomlistgenerator()

runthemainprogram(randomlist_thousand)

runthemainprogram(randomlist_tenthousand)

runthemainprogram(randomlist_thirtythousand)

Simple_positiveList = [101.02, 94.012, 20, 33, 5, 8, 666, 235]
Simple_negativeList = [101.02, 94.012, 20.05, 33.03, 5.99, -1234.33, -54.130, -394.304, 442, 1024, 503, -421, 999]
'''testing with a small list'''
sortedlist = runthemainprogram(Simple_negativeList)
print(sortedlist)

'''
Bucket Sort uses Buckets as extra space to fill in the index numbers, these buckets could be infinite long (k), which makes the 
space complexity: O(n+k)
The steps are approximatly: 12+ 16N + 2N^2 + 2Log(n) + 2N*Log(n)
Which gives n*Log(n) as Big O
'''