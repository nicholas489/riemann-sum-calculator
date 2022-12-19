# Riemann Sum Calculator (for every polynomial Parent Function or y = ax^n + z for a,x,z existing as integers)
import math
import sys

file = open("output.txt", "w")

# Need to calculate the area under a specific function
def f(x):
    # Initialize empty lists/strings to extract the integer values from our string
    coefficients = []
    powers = []
    pureNumber = []
    parsed = ""
    # Get rid of all spaces of the function inputted by the user
    for i in func:
        if i != " ":
            parsed += i
    # The function inputted by the user exceeds the single term of the "x" variable
    if parsed.count("x") >= 2:
        raise ValueError("Your function seems to be too complex. Please restart this program")
        sys.exit()
    # Parent functions: Square/Cube root x, Base Trigonometric functions, Absolute x, 2^x or e^x
    elif parsed == "x**1/2" or parsed == "x**(1/2)":
        return x**(1/2)
    elif parsed == "x**1/3" or parsed == "x**(1/3)":
        return x**(1/3)
    elif parsed == "sin(x)":
        return math.sin(x)
    elif parsed == "cos(x)":
        return math.cos(x)
    elif parsed == "tan(x)":
        return math.tan(x)
    elif parsed == "sec(x)":
        return 1 / math.cos(x)
    elif parsed == "csc(x)":
        return 1 / math.sin(x)
    elif parsed == "cot(x)":
        return 1 / math.tan(x)
    elif parsed == "|x|":
        return math.fabs(x)
    elif parsed == "2^x":
        return math.exp2(x)
    elif parsed == "e^x":
        return math.exp(x)
    # Polynomial functions of the form ax^n + z
    else:    
        for i in range(len(parsed)):
            # If any of the ASCII values found in string func are not a space, a digit, exponent("^"), plus("+"), minus("-") or "x", terminate the program 
            if ord(parsed[i]) not in [32, 43, 45, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 94, 120]:
                raise ValueError("Your function seems to be too complex. Please restart this program")
                sys.exit()
        # Edge case: Constant function
        if parsed.count("x") == 0:
            coefficients.append(int(parsed))
            powers.append(0)
            pureNumber.append(0)
        
        # Extracts the coefficient (a) on the x-term
        a = parsed.split("x") 
        try:
            coefficients.append(int(a[0]))
        except ValueError:
            coefficients.append(1)
        
        # Extracts the power on the x-term (n) and the constant (z)
        # Case 1: There is no "n" in the inputted function 
        if parsed.count("^") == 0: # There is no power term, meaning we can raise x^1 and mathematically it'd still be the same thing. Plus everything after the x term is constant (z)
            try:
                powers.append(1)
                pureNumber.append(int(parsed[parsed.find("x") + 1:]))
            except:
                print("Your function seems to be too complex. Please restart this program")
                sys.exit()
            return coefficients[0] * (x ** powers[0]) + pureNumber[0]   
        # Case 2: "n" & "z" are both positive integers
        elif parsed.count("^") == 1 and parsed.count("+") == 1:
            try:
                powers.append(int(parsed[parsed.find("^") + 1:parsed.find("+")]))
                pureNumber.append(int(parsed[parsed.find("+"):]))
            except:
                print("Your function seems to be too complex. Please restart this program")
                sys.exit()
            return coefficients[0] * (x ** powers[0]) + pureNumber[0]   
        # Case 3: "n" is a positive integer & "z" is a negative integer
        elif parsed.count("^") == 1 and parsed.count("+") == 0 and parsed.count("-") == 1:
            try: 
                powers.append(int(parsed[parsed.find("^") + 1:parsed.find("-")]))
                pureNumber.append(int(parsed[parsed.find("-"):]))
            except:
                print("Your function seems to be too complex. Please restart this program")
                sys.exit()
            return coefficients[0] * (x ** powers[0]) + pureNumber[0]   
        # Case 4: "n" & "z" are both negative integers
        else: 
            # Initializes empty strings, which we will concatenate our power/constant to
            powerNum = ""
            pureNum = ""
            # Everything between the 2 indexes of the negatives inside the inputted function is our power
            for i in range(parsed.find("-") + 1, len(parsed)):
                if parsed[i] == "-":
                    break
                else:
                    powerNum += parsed[i]
            try:
                powers.append(-(int(powerNum)))
            except:
                print("Your function seems to be too complex. Please restart this program")
                sys.exit()
        
            # Everything after the second negative inside the inputted function is our constant
            for j in range(len(parsed) - 1, 0, -1):
                if parsed[j] == "-":
                    break
                else:
                    pureNum += parsed[j]
            try:
                pureNumber.append(-(int(pureNum)))
            except:
                print("Your function seems to be too complex. Please restart this program")
                sys.exit()
            return coefficients[0] * (x ** powers[0]) + pureNumber[0]   

# Need to calculate the width of each subinterval for calculations        
def widthCalculation(lowerBound, upperBound, numberOfSubintervals):
    width = (upperBound - lowerBound) / (numberOfSubintervals)
    return width

# Trapezoid approximation function
def trapezoidApprox(lowerBound, upperBound, numberOfSubintervals): 
    area = 0
    width = widthCalculation(lowerBound, upperBound, numberOfSubintervals)
    for i in range(0,numberOfSubintervals):
        leftSide = lowerBound + i*width
        rightSide = lowerBound + (i+1)*width
        y1 = f(leftSide)
        y2 = f(rightSide)
        # Area of trapezoid: A = (side1 + side2) * height / 2
        area += (y1 + y2) * width / 2 
    return area   

# Left Rectangular approximation function
def leftApprox(lowerBound, upperBound, numberOfSubintervals):
    area = 0
    width = widthCalculation(lowerBound, upperBound, numberOfSubintervals)
    for i in range(0,numberOfSubintervals):
        # Left Rectangular approximation starts at the lowerBound and shifts over to the right every iteration of i multiplied by the calculatedwidth
        leftX = lowerBound + i*width
        y = f(leftX)
        # Area of a rectangle: length * width
        area += width * y
    return area    
    
# Middle Rectangular approximation function
def middleApprox(lowerBound, upperBound, numberOfSubintervals):
    area = 0
    middleX = 0
    width = widthCalculation(lowerBound, upperBound, numberOfSubintervals)
    for i in range(0,numberOfSubintervals):
        # The left side starts at the lowerbound and shifts over to the right every iteration of i multiplied by the calculatedwidth
        leftSide = lowerBound + i * width
        # The right side starts at the lowerBound + calculatedwidth and shifts over to the right every iteration of i multiplied by the calculatedwidth
        rightSide = lowerBound + (1+i) * width 
        # Midpoint formula for 1-dimension: (x1 + x2) / 2
        middleX = (leftSide + rightSide) / 2
        y = f(middleX)
        # Area of a rectangle: length * width
        area += width * y 
    return area

# Right Rectangular approximation function    
def rightApprox(lowerBound, upperBound, numberOfSubintervals):
    area = 0
    width = widthCalculation(lowerBound, upperBound, numberOfSubintervals)
    for i in range(0,numberOfSubintervals):
        # Right Rectangular approximation starts at the upperBound and shifts over to the left every iteration of i multiplied by the calculatedwidth
        rightX = upperBound - i*width
        y = f(rightX)
        # Area of a rectangle: length * width
        area += width * y
    return area 

if __name__ == "__main__":
    # Title
    print("Riemann Sum Calculator (for every polynomial Parent Function or y = ax^n + z for a,x,z existing as integers)")
    
    # Need to select one of the two possible functions
    func = input("Input a function (f(x)) = ")
    # While loop to ensure the user selects a usable function
    
    # Need to select one of the four different ways to approximate an integral with the Riemann Sum
    methodApprox = input("Choose which approximation method you would like to use (Left, Middle, Right or Trapezoid): ")
    # While loop to ensure the user selects an approximation that exists
    while (methodApprox.capitalize() != 'Left' and methodApprox.capitalize() != 'Middle' and methodApprox.capitalize() != 'Right' and methodApprox.capitalize() != 'Trapezoid'):
        methodApprox = input("Please choose an appropriate approximation: ")
    
    # Upper and Lower bound of integration on given function
    lowerBound = float(input("What is the lower bound of integration on the x-axis: "))
    upperBound = float(input("What is the upper bound of integration the x-axis: "))
    # Number of Subintervals that should be used, with the higher amount used creating a more accurate approximation
    numberOfSubintervals = int(input("How many rects/trapezoids do you want to use? "))
    
    # Recounts what the user inputted
    file.write(f"You're approximating the area under f(x) = {func} using the {methodApprox} rule; from x = {lowerBound} to x = {upperBound} using {numberOfSubintervals} rects/trapezoids \n")
    
    # The user selected the Trapezoidal Approximation Method, which works by going from a lower value to a higher value
    if methodApprox == "Trapezoid":
        # User inputted the lowerBound to be greater than the upperBound
        if upperBound < lowerBound:
            # Calculate the integral reversed, going from upperBound to lowerBound 
            answer = round(trapezoidApprox(upperBound, lowerBound, numberOfSubintervals), 4)
            file.write(f"The approximate Integral is {answer} units^2")
        # User inputted the lowerBound to be less than the upperBound
        else:
            # Calculate the integral normally, going from lowerBound to upperBound
            answer = round(trapezoidApprox(lowerBound, upperBound, numberOfSubintervals), 4)
            file.write(f"The approximate Integral is {answer} units^2")
    
    # The user selected the Left Rectangular Approximation Method, which works by going from a lower value to a higher value
    elif methodApprox == "Left":
        # User inputted the lowerBound to be greater than the upperBound
        if upperBound < lowerBound:
            # Calculate the integral reversed, going from upperBound to lowerBound 
            answer = round(leftApprox(upperBound, lowerBound, numberOfSubintervals), 4)
            file.write(f"The approximate Integral is {answer} units^2")
        # User inputted the lowerBound to be less than the upperBound
        else:
            # Calculate the integral normally, going from lowerBound to upperBound
            answer = round(leftApprox(lowerBound, upperBound, numberOfSubintervals), 4)
            file.write(f"The approximate Integral is {answer} units^2")
    
    # The user selected the Middle Rectangular Approximation Method, which works by going from a lower value to a higher value
    elif methodApprox == "Middle":
        # User inputted the lowerBound to be greater than the upperBound
        if upperBound < lowerBound:
            # Calculate the integral reversed, going from upperBound to lowerBound 
            answer = round(middleApprox(upperBound, lowerBound, numberOfSubintervals), 4)
            file.write(f"The approximate Integral is {answer} units^2")
        # User inputted the lowerBound to be less than the upperBound
        else:
            # Calculate the integral normally, going from lowerBound to upperBound
            answer = round(middleApprox(lowerBound, upperBound, numberOfSubintervals), 4)
            file.write(f"The approximate Integral is {answer} units^2")
    
    # The user selected the Right Rectangular Approximation Method, which works by going from a lower value to a higher value
    else:
        # User inputted the lowerBound to be greater than the upperBound
        if upperBound < lowerBound:
            # Calculate the integral reversed, going from upperBound to lowerBound 
            answer = round(rightApprox(upperBound, lowerBound, numberOfSubintervals), 4)
            file.write(f"The approximate Integral is {answer} units^2")
        # User inputted the lowerBound to be less than the upperBound
        else:
            # Calculate the integral normally, going from lowerBound to upperBound
            answer = round(rightApprox(lowerBound, upperBound, numberOfSubintervals), 4)
            file.write(f"The approximate Integral is {answer} units^2")

file.close()
