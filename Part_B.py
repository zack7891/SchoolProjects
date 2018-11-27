#Part B
#This program converts name into numeric value

#Assigned my name to name variable and converted the characters to lower case
name = "Zachary Baker".lower()
#Returns sum of letters in name as numeric value 
print(sum(ord(ch) - 96 for ch in name))

