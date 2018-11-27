def main():
    #This is a program to show how a chaotic function is created
    print("This program illustrates a chaotic function")
    #Asking user to input how many numbers they want the program to output
    n = eval(input("How many numbers should I print? "))
    #Asking user to input a number to use in equation
    x = eval(input("Enter a number between 0 and 1: "))
    #Declaration for range of numbers to output
    for i in range(n):
        #Equation for 'x' input to 'x' output 
        x = 2.0 * x * (1 - x)
        #Prints 'x' output
        print (x)
#To prevent premature closing
input("Press Enter to Close")
