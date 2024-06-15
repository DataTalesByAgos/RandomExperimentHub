""" myList = list(['append','count','extend','index','pop','remove','reverse','sort'])

myTuple = tuple(['count','index'])

print('This is my list: ', myList)
print('and this tuple: ', myTuple)

for e in range(len(myList)):
    print('\n --------------- \n Function: ', myList[e])
    print(myList[e].__doc__,' \n --------------\n \n')

 """
 
arr = [
    "a",
    "b", "b",
    "c", "c", "c",
    "d", "d", "d", "d",
    "e", "e", "e", "e", "e"
]

target = input('Enter a letter to search for coincides: ')

positions = [i for i, val in enumerate(arr) if val == target]

print(positions)
