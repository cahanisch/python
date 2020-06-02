import random

def merge(left, right):
    sorted = []
    #loop adds to sorted list and then cuts down the list that were sent in
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            sorted.append(left[0])
            left.remove(left[0])
        else:
            sorted.append(right[0])
            right.remove(right[0])
    #checks to see if the left list has any elements left
    if len(left) == 0:
        sorted += right
    #checks to see if the right list has any elements left
    else:
        sorted += left
    return sorted

def mergeSort(myList):
    if len(myList) > 1:
        #divide list
        left, right = myList[:len(myList)//2], myList[len(myList)//2:]
        #continually break down the list
        left = mergeSort(left)
        right = mergeSort(right)
        #merge list section back together
        return merge(left, right)
    else:
        return myList

def quickSort(myList):
    left = []
    right =[]
    pivot = []
    #returns list once broken down far enough
    if len(myList) < 2:
        return myList
    else:
        #randomly assign a pivot point
        randNum = random.randint(0, len(myList) - 1)
        pivot.append(myList[randNum])
        myList.remove(pivot[0])
        #separing list based on pivot point
        for i in myList:
            if i < pivot[0]:
                left.append(i)
            elif i >= pivot[0]:
                right.append(i)
        return quickSort(left) + pivot + quickSort(right)
    #returns final sorted list
    return myList


def main():
    myList = [8, 6, 7, 5, 3, 0, 9, 13, 37, 73, 31, 86, 75, 30, 9, 9, 9, 867, 530, 99, 1337, 143, 313, 867, 5309, 8675309, 13337, 133337, 133, 337, 42, 42]
    print("Original  :", myList)
    print("Merge sort:", mergeSort(myList))
    print("Quick sort:", quickSort(myList))

main()