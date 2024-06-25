#CS50 problemSet3.Fuel
#Variant practicing OOP
class FuelGauge:
    def __init__(self):
        self.prompt = "Fraction: "

    def parse_fraction(self, fraction):
        try:
            x, y = map(int, fraction.split('/'))
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError
            return x, y
        except ValueError:
            raise ValueError("Invalid input")
        except ZeroDivisionError:
            raise ZeroDivisionError("Cannot divide by zero")

    def calculate_percentage(self, x, y):
        return round((x / y) * 100)

    def determine_output(self, percentage):
        if percentage <= 1:
            return "E"
        elif percentage >= 99:
            return "F"
        else:
            return f"{percentage}%"

    def run(self):
        while True:
            fraction = input(self.prompt)
            try:
                x, y = self.parse_fraction(fraction)
                percentage = self.calculate_percentage(x, y)
                print(self.determine_output(percentage))
                break
            except (ValueError, ZeroDivisionError):
                pass

if __name__ == "__main__":
    fuel_gauge = FuelGauge()
    fuel_gauge.run()