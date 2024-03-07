import math

# Need to calculate the area under a specific function
def f(x, func):
    func = func.replace(" ", "")
    # Parent functions: Square/Cube root x, Base Trigonometric functions, Absolute x, 2^x or e^x
    special_cases = {
        "x**1/2": x ** 0.5,
        "x**(1/2)": x ** 0.5,
        "x**1/3": x ** (1/3),
        "x**(1/3)": x ** (1/3),
        "sin(x)": math.sin(x),
        "cos(x)": math.cos(x),
        "tan(x)": math.tan(x),
        "sec(x)": 1 / math.cos(x),
        "csc(x)": 1 / math.sin(x),
        "cot(x)": 1 / math.tan(x),
        "|x|": abs(x),
        "2^x": 2 ** x,
        "e^x": math.exp(x)
    }
    if func in special_cases:
        return special_cases[func]
    elif 'x' not in func: # Edge case 1: Constant function
        return float(func)
    else:
        parts = func.split('x')
        coeff = float(parts[0]) if parts[0] else 1
        if len(parts) == 1 or parts[1] == '':
            power = 1
        else:
            power = float(parts[1][1:])
        return coeff * (x ** power)

# Need to calculate the width of each subinterval for calculations        
def widthCalculation(lowerBound, upperBound, numberOfSubintervals):
    return (upperBound - lowerBound) / numberOfSubintervals

# Trapezoid approximation function
def trapezoidApprox(func, lowerBound, upperBound, numberOfSubintervals): 
    area = 0
    width = widthCalculation(lowerBound, upperBound, numberOfSubintervals)
    for i in range(numberOfSubintervals):
        leftSide = lowerBound + i * width
        rightSide = leftSide + width
        # Area of trapezoid: A = (side1 + side2) * height / 2
        area += (f(leftSide, func) + f(rightSide, func)) * width / 2
    return area

# Left Rectangular approximation function
def leftApprox(func, lowerBound, upperBound, numberOfSubintervals):
    area = 0
    width = widthCalculation(lowerBound, upperBound, numberOfSubintervals)
    for i in range(numberOfSubintervals):
        x = lowerBound + i * width
        # Area of a rectangle: length * width
        area += f(x, func) * width
    return area    

# Middle Rectangular approximation function
def middleApprox(func, lowerBound, upperBound, numberOfSubintervals):
    area = 0
    width = widthCalculation(lowerBound, upperBound, numberOfSubintervals)
    for i in range(numberOfSubintervals):
        x = lowerBound + (i + 0.5) * width
        # Area of a rectangle: length * width
        area += f(x, func) * width
    return area

# Right Rectangular approximation function    
def rightApprox(func, lowerBound, upperBound, numberOfSubintervals):
    area = 0
    width = widthCalculation(lowerBound, upperBound, numberOfSubintervals)
    for i in range(numberOfSubintervals):
        x = lowerBound + (i + 1) * width
        # Area of a rectangle: length * width
        area += f(x, func) * width
    return area 

def main():
    # Title
    print("Riemann Sum Calculator (for every polynomial Parent Function or y = ax^n + z for a,x,z existing as integers)")
    
    # Need to select a function from the user
    func = input("Input a function (f(x)) = ")
    
    # Need to select one of the four different ways to approximate an integral with the Riemann Sum
    methodApprox = input("Choose which approximation method you would like to use (Left, Middle, Right or Trapezoid): ")
    # While loop to ensure the user selects an approximation that exists
    while methodApprox.capitalize() not in ['Left', 'Middle', 'Right', 'Trapezoid']:
        methodApprox = input("Please choose an appropriate approximation: ")
    
    # Upper and Lower bound of integration on given function
    lowerBound = float(input("What is the lower bound of integration on the x-axis: "))
    upperBound = float(input("What is the upper bound of integration the x-axis: "))
    # Number of Subintervals that should be used, with the higher amount used creating a more accurate approximation
    numberOfSubintervals = int(input("How many rects/trapezoids do you want to use? "))

    approximation_methods = {
        "Left": leftApprox,
        "Middle": middleApprox,
        "Right": rightApprox,
        "Trapezoid": trapezoidApprox
    }
    approx_function = approximation_methods[methodApprox.capitalize()]
    answer = round(approx_function(func, lowerBound, upperBound, numberOfSubintervals), 4)

    with open("output.txt", "w") as file:
        file.write(f"You're approximating the area under f(x) = {func} using the {methodApprox} rule; from x = {lowerBound} to x = {upperBound} using {numberOfSubintervals} rects/trapezoids \n")
        file.write(f"The approximate Integral is {answer} units^2")

if __name__ == "__main__":
    main()
