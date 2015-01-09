#Lewis Travers
#09/01/2015
#Bubble Sort


unsorted_list = ["a", "d", "c", "e", "b", "f"]

def bubble_sort(unsorted_list):
    list_sorted = False
    count = 0
    count2 = 1
    while list_sorted == False:
        if unsorted_list[count] > unsorted_list[count2]:
            temp = unsorted_list[count]
            unsorted_list[count] = unsorted_list[count2]
            unsorted_list[count2] = temp

        count = count + 1
        count2 = count2 + 1
        if count = len(unsorted_list):
            list_sorted = True
            sorted_list = unsorted_list     
    return sorted_list

#main program

