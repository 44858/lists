#Lewis Travers
#09/01/2015
#Linear Search

search_list = ["person 1", "person 2","person 3", "person 4", "person 5", "person 6"]

def details():
    search_item = input("Please enter the item that you would like to search for: ")
    return search_item

def linear_search(search_list, search_item):
    found = False
    count = 0
    while found == False and count < len(search_list):
        if search_list[count] == search_item:
            print("Found")
            found = True
        else:
            print("Not found")
        count = count + 1
    return found

# main program

search_item = details()
search_result = linear_search(search_list, search_item)
print(search_result)

    
