from plugable_calculator import Calculator

if __name__ == "__main__":
    print("*****Calculator*****")
    num_1 = float(input("First number: "))
    num_2 = float(input("Second number: "))
    op = input("Operator: ")

    calc = Calculator(num_1, num_2, op)
    print("Result {}".format(calc.calc()))