#Lewis Travers
#06/01/2015
#kill/death table

players =[
    ["k1llmAchine", 51, 49],
    ["bob2247", 5, 99],
    ["hAxOr12", 72, 30]
]



def table_function(players):
    print("-"*21)
    for player in players:
        print("|{0:>11}|{1:>3}|{2:>3}|".format(player[0], player[1], player[2]))
        print("-"*21)


#main program

table = table_function(players)
print(table)
