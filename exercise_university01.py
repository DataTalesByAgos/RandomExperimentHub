#1) Calculate the area of a triangle given the base and the height.
def area_triangle(base, height):
    return (base * height) / 2

#2) Given a number, calculate its square.
def calc_square(num):
    return num * num

#3) Convert meters to inches (1 meter = 39.37 inches)
def conv_inches(meters):
    return meters * 39.37

#4) Calculate the perimeter and the area of a rectangle given the base and the height.
def perimeter_rectangle(base, height):
    return 2 * (base + height)

def area_rectangle(base, height):
    return base * height

#5) Calculate the perimeter and the area of a circle given the radius.
def perimeter_circle(radius):
    return 2 * 3.14159 * radius

def area_circle(radius):
    return 3.14159 * radius**2

#6) Determine the hypotenuse of a right triangle given the lengths of the legs.
def calc_hypotenuse(leg1, leg2):
    return (leg1**2 + leg2**2) ** 0.5

#7) Design an algorithm that calculates the area of a triangle based on the lengths of its sides: AREA = √ P * (P - A) * (P - B) * (P - C) where P = (A + B + C) / 2
def area_triangle_sides(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

#8) Calculate the product of two natural numbers.
def product_nat(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("The entered numbers must be natural")
    return a * b

#9) Determine the largest of three integers.
def largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

#10) Calculate the integer quotient and the remainder of dividing two natural numbers a and b with a greater than or equal to b.
def quotient_remainder(a, b):
    if a < b:
        raise ValueError("The first number entered must be greater than or equal to the second")
    quotient = a // b
    remainder = a % b
    return quotient, remainder

# Print Results
print("\nExercise 1: Calculate the area of a triangle given the base and the height.")
print(area_triangle(5, 4))

print("\nExercise 2: Given a number, calculate its square.")
print(calc_square(4))

print("\nExercise 3: Convert meters to inches (1 meter = 39.37 inches)")
print(conv_inches(2))

print("\nExercise 4: Calculate the perimeter and the area of a rectangle given the base and the height.")
print("Perimeter: ", perimeter_rectangle(4, 5))
print("Area: ", area_rectangle(4, 5))

print("\nExercise 5: Calculate the perimeter and the area of a circle given the radius.")
print("Perimeter: ", perimeter_circle(3))
print("Area: ", area_circle(3))

print("\nExercise 6: Determine the hypotenuse of a right triangle given the lengths of the legs.")
print(calc_hypotenuse(3, 4))

print("\nExercise 7: Design an algorithm that calculates the area of a triangle based on the lengths of its sides.")
print(area_triangle_sides(5, 6, 7))

print("\nExercise 8: Calculate the product of two natural numbers.")
print(product_nat(4, 5))

print("\nExercise 9: Determine the largest of three integers.")
print(largest(5, 8, 2))

print("\nExercise 10: Calculate the integer quotient and the remainder of dividing two natural numbers a and b with a greater than or equal to b.")
print(quotient_remainder(10, 3))
