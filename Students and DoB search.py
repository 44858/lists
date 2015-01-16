#Lewis Travers
#16/01/2015
#Students and DoB search

names = ["John", "Sam", "Joe", "Harry", "Robert"]
dobs = ["15/12/1997", "07/08/1996", "06/02/1997", "12/03/1996", "07/10/1997"]

def search_input():
    search_item = input("Please enter the first name of the student that you would like to search for: ")
    return search_item

def linear_search(names, dobs, search_item):
    found = False
    count = 0
    while not found and count < len(names):
        if names[count] == search_item:
            print("The student's Date of Birth is {0}.".format(dobs[count]))
            found = True
        else:
            print("Student not found")
        count = count + 1

#main program

search_item = search_input()
search = linear_search(names, dobs, search_item)
print(search)
