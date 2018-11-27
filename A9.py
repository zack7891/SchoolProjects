#This is a program to tell a user what number is prime from their intial input
def Prime_Number():
        #while True:
        #try:
              a = int(input('Please enter a number between 1-100: '))
            #if a > 100:
                  #raise ValueError
             # except ValueError:
                  #print("1-100!")
                    #continue
             #else:
              #I was trying to make an augment loop to check if the number entered was between 1-100
             
              prime = [True for i in range(a+1)]
              b = 2

              while (b * b <= a): 
                  if (prime[b] ==  True):
                      for i in range(b * 2, a+1, b): 
                          prime[i] = False
                  b += 1

              for b in range(2, a): 
                  if prime[b]:
                      print(b),

       
Prime_Number()
