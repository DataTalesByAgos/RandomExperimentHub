'''
1)Swapping the values of 3 variables, A, B, and C, such that:

a. A takes the initial value of B
b. B takes the initial value of C
c. C takes the initial value of A

Indicate the necessary transfer operations using only 1 auxiliary variable.

2)Calculate the distance traveled (m) by a vehicle that has a constant speed (m/s) over a time t (s), considering it is Uniform Rectilinear Motion (URM).

3)Develop an algorithm that requests the number of correct, incorrect, and blank answers corresponding to applicants, and shows their final score considering that each correct answer has 3 points, incorrect answers have -1 point, and blank answers have 0 points.

4)Develop an algorithm that allows entering the number of won, lost, and drawn matches by ABC club in the opening tournament, and shows their total score, considering that each won match gets 3 points, a drawn match gets 1 point, and a lost match gets 0 points.

5)Solve a problem for a gas station. The dispensers record what they "dispense" in gallons, but the gasoline price is set in liters. The DF must calculate and print what to charge the customer.

6)Calculate the amount to pay for an item if the input data is the number of dozens bought and the cost per unit of this item.

7)Convert miles to kilometers. It is known that one mile is equivalent to 1.609344 kilometers.

8)Construct the solution so that given the student's grade, it writes "passed" if the grade is greater than 10.

9)Given a worker's salary, apply a 15% increase if their salary is less than $1000. Print the salary they will receive.
'''

#1)
def swap(A, B, C):
    aux = A
    A = B
    B = C
    C = aux
    return A, B, C

#2)
def swap_two(A, B, C):
    A, B, C = B, C, A
    return A, B, C

#3)
def calc_distance(v, t):
    return v * t

#4)
def calculate_score(correct, incorrect, blank):
    score = correct * 3 + incorrect * (-1) + blank * 0
    return score

#5)
def matches(won, lost, drawn):
    score = won * 3 + drawn * 1 + lost * 0
    return score

#6)
def calc_gasoline(gal, price_per_liter):
    calculated = gal * 3.78541
    return price_per_liter * calculated

#7)
def calc_payment(quantity, cost):
    return quantity * 12 * cost

#8)
def convert_miles(miles):
    return miles * 1.609344

#9)
def grade(nota):
    if nota > 10:
        return "Passed"
    else:
        return "Failed"

#10)
def salary_increase(salary):
    if salary < 1000:
        return salary + salary * 0.15
    else:
        return 0

# Print Results
print("1) Swap the values of 3 variables, A, B, and C, such that:\na. A takes the initial value of B\nb. B takes the initial value of C\nc. C takes the initial value of A")
A, B, C = 1, 2, 3
print("Initial values: ", A, " ", B, " ", C, ".")
A, B, C = swap(1, 2, 3)
print("Swapped values: A =", A, "/ B =", B, "/ C =", C)

print("\n2) Indicate the necessary transfer operations using only 1 auxiliary variable")
A, B, C = swap_two(1, 2, 3)
print("Swapped values: A =", A, "/ B =", B, "/ C =", C)

print("\n3) Calculate the distance traveled (m) by a vehicle that has a constant speed (m/s) over a time t (s), considering it is Uniform Rectilinear Motion (URM)")
distance = calc_distance(10, 3)
print("The distance traveled is: ", distance, "m.")

print("\n4) Develop an algorithm that requests the number of correct, incorrect, and blank answers corresponding to applicants, and shows their final score considering that each correct answer has 3 points, incorrect answers have -1 point, and blank answers have 0 points")

correct = int(input("Enter the number of correct answers: "))
incorrect = int(input("Enter the number of incorrect answers: "))
blank = int(input("Enter the number of blank answers: "))
score = calculate_score(correct, incorrect, blank)

print("The final score is: ", score)

print("\n5) Develop an algorithm that allows entering the number of won, lost, and drawn matches by ABC club in the opening tournament, and shows their total score, considering that each won match gets 3 points, a drawn match gets 1 point, and a lost match gets 0 points.")
won = int(input("Enter the number of matches won: "))
drawn = int(input("Enter the number of matches drawn: "))
lost = int(input("Enter the number of matches lost: "))

score = matches(won, lost, drawn)
print("The final score for the matches is: ", score)

print("\n6) Solve a problem for a gas station. The dispensers record what they 'dispense' in gallons, but the gasoline price is set in liters. The DF must calculate and print what to charge the customer.")
gal = float(input("Enter the amount of gallons dispensed: "))
price_per_liter = float(input("Enter the price of gasoline per liter: "))

print("The amount to charge is: ${:.2f}".format(calc_gasoline(gal, price_per_liter)))

print("\n7) Calculate the amount to pay for an item if the input data is the number of dozens bought and the cost per unit of this item.")
quantity = int(input("Enter the quantity of products in dozens to be bought: "))
cost = float(input("Enter the unit cost: "))

print("The amount to pay is: ${:.2f}".format(calc_payment(quantity, cost)))

print("\n8) Convert miles to kilometers. It is known that one mile is equivalent to 1.609344 kilometers.")
miles = float(input("Enter the number of miles to convert to Km: "))

print("The equivalent in Km is: {:.2f} Km".format(convert_miles(miles)))

print("\n9) Construct the solution so that given the student's grade, it writes 'passed' if the grade is greater than 10.")
grade = int(input("Enter the student's grade: "))

print(grade(grade))

print("\n10) Given a worker's salary, apply a 15% increase if their salary is less than $1000. Print the salary they will receive.")
salary = 999
print("The salary they will receive is: ", salary_increase(salary))
