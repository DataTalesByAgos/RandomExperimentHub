def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not (2 <= len(s) <= 6):
        print(f"Length check failed for '{s}'")
        return False
    
    elif len(s) > 3 and s[2].isalpha() and s[3].isalpha():
        print(f"Alphabetic characters found at positions 2 and 3 for '{s}'")
        return True
    else:
        print(f"Failed for '{s}'")
        return False
    
if __name__ == "__main__":
    main()
    
    
    
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False

    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    if not s.isalnum():
        return False

    has_number = False
    for i, char in enumerate(s):
        if char.isdigit():
            if char == '0' and (i == 0 or (i > 0 and s[i-1].isalpha())):
                return False
            has_number = True
        elif has_number:
            return False

    return True

if __name__ == "__main__":
    main()
