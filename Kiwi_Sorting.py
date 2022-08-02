import pandas as pd 
kiwi_info = pd.read_csv("Kiwi.csv")
print (kiwi_info)
print(kiwi_info["Weight(kg)"])
kiwi_weight = kiwi_info["Weight(kg)"].tolist()
print (kiwi_weight)

kiwi_weight1 = kiwi_weight
kiwi_weight2 = kiwi_weight
kiwi_weight3 = kiwi_weight


#sr4 bubblesort for weights
def bubbleSort (kiwi_weight1):
    for i in range (0, len(kiwi_weight1) - 1): 
        for j in range (0, len(kiwi_weight1) -1-i):
            if kiwi_weight1[j] > kiwi_weight1[j+1]:
                kiwi_weight1[j], kiwi_weight1[j+1] = kiwi_weight1[j+1], kiwi_weight1[j]
    return kiwi_weight1
bubblesorted_weight = bubbleSort(kiwi_weight1)
print (bubblesorted_weight)

#sr5 selectionsort 
def selection_sort(kiwis_weight2):
    for i in range (0, len(kiwis_weight2)-1):
        minIndex = i 
        for j in range (i+1, len(kiwis_weight2)):
            if kiwis_weight2[j] < kiwis_weight2[i]:
                minIndex = j 
                if minIndex != i:
                    kiwis_weight2 [i], kiwis_weight2 [j] = kiwis_weight2 [j], kiwis_weight2[i]
    return kiwis_weight2
selectionsorted_weight = selection_sort(kiwi_weight2)
print (selectionsorted_weight)

#sr6 insertion sort 
def insertion_sort(kiwi_weight3):
    for i in range (1, len(kiwi_weight3)):
        j = i - 1
        next_e = kiwi_weight3[i]
        
        while (kiwi_weight3[j] > next_e) and (j >=0):
            kiwi_weight3[j+1] = kiwi_weight3[j]
            j=j-1
            kiwi_weight3[j+1] = next_e
    return kiwi_weight3
insertionsorted_weight = insertion_sort(kiwi_weight3)
print (insertionsorted_weight)

#sr10 
import matplotlib.pyplot as plt
plt.plot(insertionsorted_weight)
plt.ylabel('kiwiweights')
plt.show()

plt.plot(kiwi_info["Weight(kg)"].tolist(), 'ro')

plt.show()
