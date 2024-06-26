'''
In a file called grocery.py, implement a program that prompts the user for items, one per line,
until the user inputs control-d (which is a common way of ending one’s input to a program).
Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing
each line with the number of times the user inputted that item. No need to pluralize the items.
Treat the user’s input case-insensitively.

'''
items = []

def main():
    count = {}
    res = []

    while True:
        try:
            entry = input("").upper()
            if entry:
                if entry in count:
                    count[entry] += 1
                else:
                    count[entry] = 1
        except EOFError:
            break

    for e, total in count.items():
        res.append(f"{total} {e}")

    res.sort(key= lambda x: x.split(" ", 1)[1])

    for e in res:
        print(e)

if __name__ == "__main__":
    main()