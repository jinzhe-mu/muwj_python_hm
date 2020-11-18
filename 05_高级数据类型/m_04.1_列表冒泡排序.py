num_list = [2, 5, 9, 22, 1, 98, 25]

cow = 0
col = cow + 1
cont = 0

while cow < len(num_list):

    while col < len(num_list):

        print(num_list)

        if num_list[cow] <= num_list[col]:
            cont = num_list[col]
            num_list[col] = num_list[cow]
            num_list[cow] = cont
        col += 1

    cow += 1
    col = cow + 1

print(num_list)

