#Erik Rivera
#11/11/24
#Last Name Letters

#Code reference from https://www.w3schools.com/python/

firstName = "Erik"
# gets sentence from user
sentence = input("Please enter your sentence here: ")

#Stores letters found in sentence that are in first name
sameLetters = ""

#Initials the letter counter for the first name
lettersCount = 0

#For loop through the sentence
for char in sentence:
    if char.lower() in firstName.lower(): #Checks if letter in sentence
        sameLetters = sameLetters + char #Adds the letter found to the empty string
        lettersCount = lettersCount + 1 #Increases the number every time a letter is found
 
#Prints the total of all of the letters that were found   
print(sameLetters)
print("There were " + str(lettersCount) + " in that sentence that shared letters of my first name - Erik.")


        

