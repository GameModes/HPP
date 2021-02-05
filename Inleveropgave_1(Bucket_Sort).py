import time
import math
import random


def getbetterlist(simplelist):
    """
    :param simplelist:
    :return: list containing elements with same length
    """
    def getdecimallist(lst):
        """
        :param lst:
        :return: list containing elements with same length behind (decimals)
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
    """
    negative_betterlist = [y for y in lst if float(y) < 0]
    positive_betterlist = [x for x in lst if float(x) > 0]
    return negative_betterlist, positive_betterlist

def Ihasabucket(betterlist):
    """

    :param betterlist:
    :return: a sorted list
    """
    characters = len(betterlist[0])
    for character in range(characters):
        buckets = [[], [], [], [], [], [], [], [], [], []]
        character = characters - character
        for index in range(len(betterlist)):
            if betterlist[index][character - 1] != '.' and betterlist[index][character - 1] != '-':
                buckets[int(betterlist[index][character - 1])].append(betterlist[index])

        if buckets != [[], [], [], [], [], [], [], [], [], []]:
            if any(float(n) < 0 for n in betterlist):
                buckets.reverse()
            newplaced = [y for x in buckets for y in x]
            betterlist = newplaced
    return betterlist


def runthebucketsort(lst):
    """

    :param lst:
    :return:
    """
    start = time.time()
    print("Using  getbetterlist function on simple list...")
    betterlist = getbetterlist(lst)
    print("Done!")
    if any(float(n) < 0 for n in betterlist):
        print("Contains negatives")
        print("Splits values...")
        negative_betterlist, positive_betterlist = positiv_negative_split(betterlist)
        print("Done!")
        print("Uses Bucket Sort on positive better list...")
        sorted_positive_list = Ihasabucket(positive_betterlist)
        rounded_sorted_positive_list = [round(float(num)) for num in sorted_positive_list]
        print("Done!")
        print("Uses Bucket Sort on negative better list...")
        sorted_negative_list = Ihasabucket(negative_betterlist)
        rounded_negative_positive_list = [round(float(num)) for num in sorted_negative_list]
        print("Done!")
        print("Adding Together...")
        sortedlist = rounded_negative_positive_list + rounded_sorted_positive_list
        print("Done!")
    else:
        print("Contains non negatives")
        print("Uses Bucket Sort on better list...")
        sortedlist = Ihasabucket(betterlist)
        print("Done!")
    print('It took: ' + str(time.time() - start) + ' seconds\n')
    return sortedlist

def randomlistgenerator():
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

Simple_positiveList = [101.02, 94.012, 20, 33, 5]
Simple_negativeList = [101.02, 94.012, 20, 33, 5, -1234, -13, -394]
randomlist_thousand, randomlist_tenthousand, randomlist_thirtythousand = randomlistgenerator()


runthebucketsort(randomlist_thousand)

runthebucketsort(randomlist_tenthousand)

runthebucketsort(randomlist_thirtythousand)
