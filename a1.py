# Riemann Sum Calculator (for only f(x) = x or f(x) = x^2)
# Problem: It is very tedious writing out the entire solution to approximating simple integrals using the Riemann Sum

file = open("output.txt", "w")

# Need to calculate the area under a specific function
def f(x):
    # User inputs 'x' as a string, return x
    if func == 'x':
        return x
    # User inputs 'x^2' as a string, return x**2
    elif func == 'x^2':
        return x ** 2

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
    print("Riemann Sum Calculator for y = x and y = x^2")
    
    # Need to select one of the two possible functions
    func = input("Input a function (f(x)) = ")
    # While loop to ensure the user selects a usable function
    while (func == 'x' or func == 'x^2') == False:
        func = input("Please input a Linear/Quadratic function (f(x)) = ")
    
    # Need to select one of the four different ways to approximate an integral with the Riemann Sum
    methodApprox = input("Choose which approximation method you would like to use (Left, Middle, Right or Trapezoid): ")
    # While loop to ensure the user selects an approximation that exists
    while (methodApprox != 'Left' and methodApprox != 'Middle' and methodApprox != 'Right' and methodApprox != 'Trapezoid'):
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
            answer = round(trapezoidApprox(upperBound, lowerBound, numberOfSubintervals), 3)
            file.write(f"The approximate Integral is {answer} units^2")
        # User inputted the lowerBound to be less than the upperBound
        else:
            # Calculate the integral normally, going from lowerBound to upperBound
            answer = round(trapezoidApprox(lowerBound, upperBound, numberOfSubintervals), 3)
            file.write(f"The approximate Integral is {answer} units^2")
    
    # The user selected the Left Rectangular Approximation Method, which works by going from a lower value to a higher value
    elif methodApprox == "Left":
        # User inputted the lowerBound to be greater than the upperBound
        if upperBound < lowerBound:
            # Calculate the integral reversed, going from upperBound to lowerBound 
            answer = round(leftApprox(upperBound, lowerBound, numberOfSubintervals), 3)
            file.write(f"The approximate Integral is {answer} units^2")
        # User inputted the lowerBound to be less than the upperBound
        else:
            # Calculate the integral normally, going from lowerBound to upperBound
            answer = round(leftApprox(lowerBound, upperBound, numberOfSubintervals), 3)
            file.write(f"The approximate Integral is {answer} units^2")
    
    # The user selected the Middle Rectangular Approximation Method, which works by going from a lower value to a higher value
    elif methodApprox == "Middle":
        # User inputted the lowerBound to be greater than the upperBound
        if upperBound < lowerBound:
            # Calculate the integral reversed, going from upperBound to lowerBound 
            answer = round(middleApprox(upperBound, lowerBound, numberOfSubintervals), 3)
            file.write(f"The approximate Integral is {answer} units^2")
        # User inputted the lowerBound to be less than the upperBound
        else:
            # Calculate the integral normally, going from lowerBound to upperBound
            answer = round(middleApprox(lowerBound, upperBound, numberOfSubintervals), 3)
            file.write((f"The approximate Integral is {answer} units^2"))
    
    # The user selected the Right Rectangular Approximation Method, which works by going from a lower value to a higher value
    else:
        # User inputted the lowerBound to be greater than the upperBound
        if upperBound < lowerBound:
            # Calculate the integral reversed, going from upperBound to lowerBound 
            answer = round(rightApprox(upperBound, lowerBound, numberOfSubintervals), 3)
            file.write(f"The approximate Integral is {answer} units^2")
        # User inputted the lowerBound to be less than the upperBound
        else:
            # Calculate the integral normally, going from lowerBound to upperBound
            answer = round(rightApprox(lowerBound, upperBound, numberOfSubintervals), 3)
            file.write(f"The approximate Integral is {answer} units^2")

file.close()
