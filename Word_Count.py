#Part A This program gets a sentence typed in by the user and returns it with the amount of words entered
#User Input
sentence = input("Please enter a sentence:")
#Assigns space between words as zero
space_count = 0
#A loop calling on space_count varible checking for spaces between words in user input
for character in sentence:
    if character == " ":
        space_count = space_count + 1
#Assigns space_count to number of words        
number_of_words = space_count + 1
#Returns sentence user entered 
print("The user entered:", sentence)
#Returns amount of words
print("The number of words in the sentence is", number_of_words)
#Added to prevent program from closing
input("Press 'Enter' key to close")
