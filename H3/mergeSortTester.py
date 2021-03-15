import time, random
import H3.MultiThreadSortingV3 as mT
import matplotlib.pyplot as plt


def sortedListPrinter(sortedList):
    """
    prints the list in the console in a viewable way
    :param sortedList:
    """
    if len(sortedList[0]) <= 40:
        print('The sorted list is: ', sortedList)
    else:
        print('The first 40 elements of sorted list are: ', sortedList[0][0:41])


def specificThreadTester(amountThreads = 4, amountOfNumbers=10000):
    '''Dit is een test om 1 specifiek hoeveelheid aan treads te gebruiken en dan te berekenen'''
    print("\nResults of specificThreadTester:")
    startTime = time.perf_counter()
    arr = [random.randrange(1, 10000, 1) for i in range(amountOfNumbers)]
    sortedList = mT.getSortedList(arr, amountThreads)
    sortedListPrinter(sortedList)
    print(f'Finished in {round(time.perf_counter() - startTime, 2)} seconds \n')

specificThreadTester(amountThreads = 9)

def threadComparisonTester(amountOfNumbers=10000, unsortedList=None):
    """
    This will test multiple threads (until 256) with the given or randomised list and saves the results of using every thread
    in variable y and plots this in a graph. (Remember that every thread might be used for something on your computer)
    :param amountOfNumbers:
    :param unsortedList:
    """
    print("\nResults of threadComparisonTester:")
    threads = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    y = []
    if unsortedList == None:
        unsortedList = [random.randrange(1, 10000, 1) for i in range(amountOfNumbers)]
    wholestarttime = time.perf_counter()

    for thread in threads:
        copyarr = unsortedList.copy()
        starttime = time.perf_counter()
        sortedList = mT.getSortedList(copyarr, thread)
        y.append(round(time.perf_counter() - starttime, 2))
        print("Amount of Threads: ", thread)
        sortedListPrinter(sortedList)
        print(f'Finished in {round(time.perf_counter() - wholestarttime, 2)} seconds \n')

    plt.plot(threads, y, linestyle='--', marker='o', color='g')
    plt.xlabel('x - Amount of Threads')
    plt.ylabel('y - Time Used')
    plotTitle = 'Time Used to sort ' + str(amountOfNumbers) +' numbers compared to amount of Threads'
    plt.title(plotTitle)
    plt.show()

threadComparisonTester()


