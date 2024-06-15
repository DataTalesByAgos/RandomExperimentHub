""" myList = list(['append','count','extend','index','pop','remove','reverse','sort'])

myTuple = tuple(['count','index'])

print('This is my list: ', myList)
print('and this tuple: ', myTuple)

for e in range(len(myList)):
    print('\n --------------- \n Function: ', myList[e])
    print(myList[e].__doc__,' \n --------------\n \n')


 
arr = [
    "a",
    "b", "b",
    "c", "c", "c",
    "d", "d", "d", "d",
    "e", "e", "e", "e", "e"
]

target = input('Enter a letter to search for coincides: ')

positions = [i for i, val in enumerate(arr) if val == target]

print(positions,'\n\n')


d = {'y':99,'a':10,'c':22,'b':1,'z':3,'h':44}
print('My dictionary: ',d,'\n')

t = sorted(d.items())
print('My sortedDictionary: ',t,'\n')

for k,v in sorted(d.items()):
    print(k,v)
 """
text = open('sample.txt')
counts = dict()

for line in text:
    words = line.split()
    for word in words:
        counts[word]= counts.get(word,0) +1
lst = list()
for k,v in counts.items():
    newtup = (v,k)
    lst.append(newtup)
    
lst = sorted(lst, reverse=True)

for v,k in lst[:10]:
    print(k,v)
    
