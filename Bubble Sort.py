#Lewis Travers
#09/01/2015
#Bubble Sort



unsorted_list = ["a", "d", "c", "e", "b", "f", "h", "g"]

def bubble_sort(unsorted_list):
    list_sorted = False
    length = len(unsorted_list) - 1
    while not list_sorted:
        list_sorted = True
        for num in range(length):
            if unsorted_list[num] > unsorted_list[num+1]:
                list_sorted = False
                unsorted_list[num], unsorted_list[num+1] = unsorted_list[num+1], unsorted_list[num]
    return unsorted_list    
       


#main program

sorted_list = bubble_sort(unsorted_list)
print(sorted_list)

