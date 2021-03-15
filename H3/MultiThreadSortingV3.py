import concurrent.futures

# Python program for implementation of MergeSort from Source: https://www.geeksforgeeks.org/merge-sort/
def mergeSort(arr):
    """
    This function sorts with the method merge the lists and returns it.
    This mergeSort method is based on using the same function over and over again so the elements in the list can easily be split into smaller ones and
    back if needed, because of using the L (Left Side) and R(Right Side) in the list
    :Param: A list that is unsorted
    :rtype: Array that is completed sorted
    """
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr) // 2
        # Dividing the array elements
        L = arr[:mid]
        # into 2 halves
        R = arr[mid:]
        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


def splitList(l, k):  # source: https://stackoverflow.com/questions/2130016/splitting-a-list-into-n-parts-of-approximately-equal-length
    """
    Splits 1 list into equally long smaller lists to seperate the lists so that the threads can use each one
    :param l: The whole list
    :param k: the amount of lists the whole list should be seperated
    :return: Multiple lists which are splitted from the whole list
    """
    n = len(l)
    return [l[i * (n // k) + min(i, n % k):(i + 1) * (n // k) + min(i + 1, n % k)] for i in range(k)]


def mergingLists(lst1, lst2):  # source: https://www.geeksforgeeks.org/python-combining-two-sorted-lists/
    """
    Merged the lists that has been split by splitList() and each added number from the 2 lists will be compared with each other to keep the list sorted
    :param lst1: list1
    :param lst2: list2
    :return: a list that has been merged with list1 and list2 using some kind of merge sort
    """
    size_1 = len(lst1)
    size_2 = len(lst2)

    res = []
    i, j = 0, 0

    while i < size_1 and j < size_2:
        if lst1[i] < lst2[j]:
            res.append(lst1[i])
            i += 1

        else:
            res.append(lst2[j])
            j += 1
    mergedList = res + lst1[i:] + lst2[j:]
    return mergedList


def getSortedList(arr, amountThreads=1):
    """
    This is the main function to use the above functions in the following order:
    1. splitList(), splits inserted list l, into k parts so it will return a lists with smaller lists e.g.: [1,2,3,4,5,6], 2 -> [[1,2,3],[4,5,6]]
    Gives every threads a splitted list using concurrent.futures so that each thread can use it in mergeSort()
    2. mergeSort(), splits the inserted list arr, into smaller pieces until they are 1 element long. They each will be added with each other and sorted at the same time.
    3. mergingLists(), merged the lists that has been split by splitList() and each added number from the 2 lists will be compared with each other to keep the list sorted
    :param arr: an unsorted list
    :param amountThreads: the amount of threads used. Default is set on 1
    :return: The sorted list
    """
    sortedMiniLists = [] #This list will be used to avoid the threads using the same variable so they must wait, which slows down the progress.
    sortedList = []

    splittedList = splitList(arr, amountThreads)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(mergeSort, splittedList[threadnumber]) for threadnumber in range(amountThreads)]

    for f in concurrent.futures.as_completed(results):
        sortedMiniLists.append(f.result())

    while len(sortedList) != 1:
        sortedList = []
        for i in range(0, len(sortedMiniLists), 2):
            try:
                sortedList.append(mergingLists(sortedMiniLists[i], sortedMiniLists[i + 1]))
            except IndexError:
                sortedList.append(sortedMiniLists[i])

        sortedMiniLists = sortedList
    return sortedList








