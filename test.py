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
text = open('sample.txt','r')
counts = dict()

for line in text:
    words = line.split()
    for i,word in enumerate(words):
        if word == 'the':
            start_index = max(0,i-2)
            end_index = min(len(words),i+3)
            context_words = words[start_index:end_index]
            context_line = ' '.join(context_words)
            print(context_line)
 
print('\n\n')           
lst = sorted([(k,v) for v,k in counts.items()], reverse =True)

for v,k in lst[:10]:
    print(k,v)
 
d = {'y':99,'a':10,'c':22,'b':1,'z':3,'h':44}

print(sorted([(v,k) for k,v in d.items()]))
print(sorted([(k,v) for k,v in d.items()]))