'''
In a file called grocery.py, implement a program that prompts the user for items, one per line,
until the user inputs control-d (which is a common way of ending one’s input to a program).
Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing
each line with the number of times the user inputted that item. No need to pluralize the items.
Treat the user’s input case-insensitively.

'''
def main():
    count = {}

    while True:
        try:
            entry = input("").upper()
            if entry:
                count[entry] = count.get(entry, 0) + 1
        except EOFError:
            break

    sorted_items = sorted(count.items())

    for item, total in sorted_items:
        print(f"{total} {item}")

if __name__ == "__main__":
    main()