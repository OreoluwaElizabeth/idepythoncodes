#multiplication = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
#for count in range(4):
    #for counter in range(5):
        #multiplication[count][counter] = count * counter
#print(multiplication)


#outer_list = []
#for count in range(4):
    #inner_list = []
    #for counter in range(5):
        #inner_list.append(count * counter)
    #outer_list.append(inner_list)
#print(outer_list)

outer_list = []
inner_list = []
for count in range(4):
    for counter in range(5):
        print(outer_list[count][counter], end= " ")
print()