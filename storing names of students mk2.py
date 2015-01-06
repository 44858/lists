#Lewis Travers 
#11/12/2014 
#storing the names of students 
 
 
def name_input(): 
    first_name = input("Please enter the name of the first student: ")
    second_name = input("Please enter the name of the second student: ") 
    third_name = input("Please enter the name of the third student: ")
    fourth_name = input("Please enter the name of the fourth student: ") 
    fifth_name = input("Please enter the name of the fifth student: ")
    
    seventh_name = input("Please enter the name of the seventh student: ") 
    eighth_name = input("Please enter the name of the eighth student: ") 
    return first_name, second_name, third_name, fourth_name, fifth_name, sixth_name, seventh_name, eighth_name 

 
def display_names(first_name, second_name, third_name, fourth_name, fifth_name, sixth_name, seventh_name, eighth_name):
    print("1. {0}".format(first_name))
    print("2. {0}".format(second_name)) 
    print("3. {0}".format(third_name)) 
    print("4. {0}".format(fourth_name)) 
    print("5. {0}".format(fifth_name)) 
    print("6. {0}".format(sixth_name)) 
    print("7. {0}".format(seventh_name))
    print("8. {0}".format(eighth_name))
   

 
def edit_input(first_name, second_name, third_name, fourth_name, fifth_name, sixth_name, seventh_name, eighth_name):
    edit = int(input("Please enter the number of the student you would like to edit: ")
    if edit == 1:
         first_name = input("Please enter the new name of the first student: ")
    elif edit == 2:
         second_name = input("Please enter the new name of the second student: ")
    elif edit == 3:
         third_name = input("Please enter the new name of the third student: ")
    elif edit == 4:
         fourth_name = input("Please enter the new name of the fourth student: ")
    elif edit == 5:
         fifth_name = input("Please enter the new name of the fifth student: ")
    elif edit == 6:
         sixth_name = input("Please enter the new name of the sixth student: ")
    elif edit == 7:
         seventh_name = input("Please enter the new name of the seventh student: ")
    elif edit == 8:
         eighth_name = input("Please enter the name of the eighth student: ")
    else:
         print("That is not a valid number.")
    

#main program

first_name, second_name, third_name, fourth_name, fifth_name, sixth_name, seventh_name, eighth_name = name_input()
names = display names(first_name, second_name, third_name, fourth_name, fifth_name, sixth_name, seventh_name, eighth_name)
print(names)
edit = edit_input(first_name, second_name, third_name, fourth_name, fifth_name, sixth_name, seventh_name, eighth_name)
print(edit)
               
