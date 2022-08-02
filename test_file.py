from random import randint, random
from Kiwi_Sorting import bubbleSort,selection_sort,insertion_sort
from time import time
 
averagecase= [randint(1,10000) for _ in range(1000)]
bestcase= sorted(averagecase)
worstcase= sorted(averagecase, reverse=True)
 
def test_BubbleWorst():
    start= time()
    assert bubbleSort(worstcase) == bestcase
    print(time()-start)
 
def test_BubbleBest():
    start= time()
    assert bubbleSort(bestcase) == bestcase
    print(time()-start)
 
def test_BubbleAvg():
    start= time()
    assert bubbleSort(averagecase) == bestcase
    print(time()-start)

#selection testing 
def test_selectionWorst():
    start= time()
    assert selection_sort(worstcase) == bestcase
    print(time()-start)
 
def test_selectionBest():
    start= time()
    assert selection_sort(bestcase) == bestcase
    print(time()-start)
 
def test_selectionAvg():
    start= time()
    assert selection_sort(averagecase) == bestcase
    print(time()-start)


#insertion testing 
def test_insertionWorst():
    start= time()
    assert insertion_sort(worstcase) == bestcase
    print(time()-start)
 
def test_insertionBest():
    start= time()
    assert insertion_sort(bestcase) == bestcase
    print(time()-start)
 
def test_insertionAvg():
    start= time()
    assert insertion_sort(averagecase) == bestcase
    print(time()-start)