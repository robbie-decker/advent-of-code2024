# Two lists
# Sort both lists
# Compare distances between lists
from functools import reduce

def get_distance(list1, list2):
    list1 = sorted(list1)
    list2 = sorted(list2)

    return (reduce(lambda x, y: x + (max(y) - min(y)), list(zip(list1, list2)), 0))



with open("input.txt", "r") as file:
    list1 = []
    list2 = []
    for line in file:
        p = line.split()
        # print(p)
        list1.append(int(p[0]))
        list2.append(int(p[1]))


# for i in range(len(list1)):
#     print(f"{list1[i]} : {list2[i]} : {i}")

get_distance(list1, list2)