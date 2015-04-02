# Name: Logan McCaul
# Email: logan.mccaul@colorado.edu
# SUID: 10662961
#

import sys
import random
import time

# --------- Insertion Sort -------------
# Implementation of getPosition
# Helper function for insertionSort
def getPosition(rList, elt):
    # Find the position where element occurs in the list
    #
    for (i,e) in enumerate(rList):
        if (e >= elt):
            return i
    return len(rList)

# Implementation of Insertion Sort 
def insertionSort(lst):
    n = len(lst)
    retList = []
    for i in lst:
        pos = getPosition(retList,i)
        retList.insert(pos,i)    
    return retList

#------ Merge Sort --------------
def mergeSort(lst):
    # TODO: Implement mergesort here
    # You can add additional utility functions to help you out.
    # But the function to do mergesort should be called mergeSort
	length = len(lst)
	if length == 1:
		return lst
	mid = length//2
	lst1 = mergeSort(lst[:mid])
	lst2 = mergeSort(lst[mid:])
	i = 0
	j = 0
	k = 0
	while i < len(lst1) and j < len(lst2):
		if lst1[i] < lst2[j]:
			lst[k] = lst1[i]
			i += 1
			k += 1
		else:
			lst[k] = lst2[j]
			j += 1
			k += 1
	while i < len(lst1):
		lst[k] = lst1[i]
		i += 1
		k += 1
	while j < len(lst2):
		lst[k] = lst2[j]
		j += 1
		k += 1
	return lst
# TODO: change this

#------ Quick Sort --------------
def quickSort(lst):
    # TODO: Implement quicksort here
    # You may add additional utility functions to help you out.
    # But the function to do quicksort should be called quickSort
	length = len(lst)
	if length <= 1:
		return lst
	rnd = random.randint(0,length-1)
	pivot = lst[rnd]
	lst1 = []
	lst2 = []
	lst3 = []
	for i in lst:
		if i < pivot:
			lst1.append(i)
		elif i > pivot:
			lst2.append(i)
		elif i == pivot:
			lst3.append(i)	
	lst1 = quickSort(lst1)
	lst2 = quickSort(lst2)
	return lst1 + lst3 + lst2 # TODO: change this
    


# ------ Timing Utility Functions ---------

# Function: generateRandomList
# Generate a list of n elements from 0 to n-1
# Shuffle these elements at random

def generateRandomList(n):
   # Generate a random shuffle of n elements
   lst = list(range(0,n))
   random.shuffle(lst)
   return lst


def measureRunningTimeComplexity(sortFunction,lst):
    t0 = time.clock()
    sortFunction(lst)
    t1 = time.clock() # A rather crude way to time the process.
    return (t1 - t0)


# --- TODO

# Write code to extract average/worst-case time complexity
def main():
	f = open('times.csv', 'w')
	for i in range(20):
		print "i ", i
		j = 5
		f.write("\n###############################################")
		while j <= 500:
			print j
			lst = generateRandomList(j)
			iS = measureRunningTimeComplexity(insertionSort, lst)
			mS = measureRunningTimeComplexity(mergeSort, lst)
			qS = measureRunningTimeComplexity(quickSort, lst)
			iS = str(iS*1000000)
			mS = str(mS*1000000)
			qS = str(qS*1000000)
			time = "\n"+iS+","+mS+","+qS
			f.write(time)
			j += 5
	f.close()
main()
