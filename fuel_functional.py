def parse_fraction(fraction):
    try:
        x, y = map(int, fraction.split('/'))
        #   parse_fraction = lambda frac: map(int, frac.split('/')) 
        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError
        return x, y
    except ValueError:
        raise ValueError("Invalid input")
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero")

def calculate_percentage(x, y):
    return round((x / y) * 100)

def determine_output(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

def main():
    while True:
        fraction = input("Fraction: ")
        try:
            x, y = parse_fraction(fraction)
            percentage = calculate_percentage(x, y)
            print(determine_output(percentage))
            break
        except (ValueError, ZeroDivisionError):
            pass

if __name__ == "__main__":
    main()