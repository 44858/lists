#Lewis Travers
#12/12/2014
#storing the names of students with lists

def list_names():
    names = ["James", "Alice", "Sarah", "Ahmed", "Richard", "Hoi", "Fraser", "Claire",]
    return names

def print_names(names):
    for count in names:
        print(count)

def edit_names(names):
    edit = input("Please enter the name of the student you would like to edit: ")
    if "James" in names:
        new_name = input("Please enter the new name of the student: ")
        names.pop(1)
        names.insert(1,new_name)
    elif "Alice" in names:
        new_name = input("Please enter the new name of the student: ")
        names.pop(2)
        names.insert(2,new_name)
    elif "Sarah" in names:
        new_name = input("Please enter the new name of the student: ")
        names.pop(3)
        names.insert(3,new_name)
    elif "Ahmed" in names:
        new_name = input("Please enter the new name of the student: ")
        names.pop(4)
        names.insert(4,new_name)
    elif "Richard" in names:
        new_name = input("Please enter the new name of the student: ")
        names.pop(5)
        names.insert(5,new_name)
    elif "Hoi" in names:
        new_name = input("Please enter the new name of the student: ")
        names.pop(6)
        names.insert(6,new_name)
    elif "Fraser" in names:
        new_name = input("Please enter the new name of the student: ")
        names.pop(7)
        names.insert(7,new_name)
    elif "Claire" in names:
        new_name = input("Please enter the new name of the student: ")
        names.pop(8)
        names.insert(8,new_name)
    return new_name
        

#main program
names = list_names()
names = print_names(names)
print(names)
new_name = edit_names(names)
print(edit)
