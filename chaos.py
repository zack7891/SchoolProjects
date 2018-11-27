def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 2.0 * x * (1 - x)
        print (x)
#To prevent premature closing
input("Press Enter to Close")
#The diffence in this program versus the first seems to be the lack of randominess it can output.
#The first program with 3.6 was able to output more random numbers than the current program.
