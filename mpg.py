def start_program():
    x = input("Do you have a file to upload?(Yes or No)")
    if x == "Yes" or x =="yes" or x == "YES":
        fileName = input("What file are the numbers in?")
        infile = open(fileName,'r')
        total = 0.0
        count = 0
        for line in infile:
            total = total + float(line)
            count = count + 1
            print("\n The total MPG for this trip is" , total / count, "MPG")
    else:
        Odometer = input("What is the starting odometer?")
        legCount = 0
        y = 0
        moredata = "yes"
        while moredata[0] == "y":
            x = (input("How many miles did you drive?"))
            y = (input("How many gallons of gas did you use?"))
            total = Odometer + x
            mpg = int(float(total) / float(y))
            legCount = legCount + 1
            moredata = input("Do you have more informatio to enter (yes or no)? ")
            print("\n The total MPG for this trip is", legCount * mpg,"MPG")
       
start_program()
'''
def main():
    Odometer = input("What is the starting odometer?")
    legCount = 0
    y = 0
    moredata = "yes"
    while moredata[0] == "y":
        x = (input("How many miles did you drive?"))
        y = (input("How many gallons of gas did you use?"))
        total = Odometer + x
        mpg = int(float(total) / float(y))
        legCount = legCount + 1
        moredata = input("Do you have more informatio to enter (yes or no)? ")
        print("\n The total MPG for this trip is", legCount * mpg,"MPG")
main()
'''
'''
def file_gas():
 fileName = input("What file are the numbers in?")
 infile = open(fileName,'r')
 total = 0.0
 count = 0
 for line in infile:
     total = total + float(line)
     count = count + 1
     print("\n The total MPG for this trip is" , total / count, "MPG")
file_gas()
'''


