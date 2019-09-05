matrix=[
    [1.2,3],
    [4,5,6],
    [7,8,9]
]
matrix[0][1]
for row in matrix:
    for item in row:
        print(item)

numbers=[1,2,3,4,5,6]
numbers.append(20)#addes at end of list
numbers.insert(0,10)
numbers.remove(5)
numbers.clear()
numbers.pop(2)
numbers.index(50)
print(50 in numbers)# search for number in lis
numbers.count(5)
numbers.sort()
print(numbers)