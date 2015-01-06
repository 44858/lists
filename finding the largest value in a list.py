#Lewis Travers
#12/12/2014
#finding the largest value in a list

values = [24, 13, 57, 45]

result = 0
index = 0
boolean = False

while boolean == False:
    index = index + 1
    if result < values[index]:
       result = values[index]
    if index == 3:
       boolean = True

for index, result in enumerate(values):
    print("{0} | {1}".format(index+1, result))
