# Creating a list with some elements

# Create a list of 10 numbers from 1 to 10
# l1 = [1,2,3,4,5,6,7,8,9,10]

l1 = list()
for i in range(1,11):
    l1.append(i)

l1 = [i for i in range(1,11)]
d1 = {k:k**2 for k in range(1,11)}
print(d1)

l2 = [i for i in range(20)]
l3 = [i**2 for i in l2 if i%2 == 0]

d2 = {'apple': 20, 'mango': 15,'grapes':25}
# list_stock = list(d2.values())
# list_items = list(d2.items())

# list_items = [(k,v) for k,v in sorted(list(d2.items()), key= lambda x: x[1])]
# for k,v in list_items:
#     print(k,v)

l1 = ['1','2','3','4']
# l2 = list()
# for i in l1:
#     l2.append(int(i))

# print(l2)

l2 = list(map(int, l1))

# numbers = list(map(int, input("Enter 5 numbers seperated by spaces: ").split()))
numbers = list(map(lambda x: int(x)**2, input("Enter 5 numbers seperated by spaces: ").split()))







