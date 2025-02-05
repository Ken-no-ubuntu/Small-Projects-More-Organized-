import random
listA = [4, 5, 10, 11, 55, 100, 10050, 65, 70, 59 ,99, 40]
n = len(listA)
x = 3
qtselect = n - x  #points to be selected
numselect = random.sample(listA, qtselect) #final selection of numbers. picked from listA, with only qtselect quantity to be picked
filtered_items = [item for item in numselect if item > 10 and item % 2 != 0]
print(f"{qtselect} items:", numselect)
print(filtered_items)