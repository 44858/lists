#Lewis Travers
#31/12/2014
#Selecting 6 random rumbers

list1 = []

for count in range(1, 20):
    list1.append(count)

boolean = False
counter = 0

while boolean == False:
    import random
    for index in enumerate(list1):
        number = random.choice(list1)
        if number != 0:
           print(number)
           list1[index]= 0
           counter = counter + 1
    if counter == 6:
        boolean = True
        
        
        
    
        




    
