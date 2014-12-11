#Lewis Travers
#11/12/2014
#storing the names of students

def name_input():
    first_name = input("Please enter the name of the first student: ")
    second_name = input("Please enter the name of the second student: ")
    third_name = input("Please enter the name of the third student: ")
    fourth_name = input("Please enter the name of the fourth student: ")
    fifth_name = input("Please enter the name of the fifth student: ")
    sixth_name = input("Please enter the name of the sixth student: ")
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

def edit_input
