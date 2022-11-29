
#For anyone who not understand, Sparx Math Bookwork system work like this:

# First, it will create a random number from 01 - 99
# And the number will be added by 10 on every question (so if you got 19 on the first question, the next question will be 29)
# When the number reach to 9 (like 91 or 98), the system will reset it and add a unit (so if it 91, 

# The letter will be the (number+1)th of the alphabet
# For example if the bookwork number is 57, the word will be (5+7+1)th letter in the alphabet, which is n (Sparx Math alphabet is very unique, it doesn't contain I,O,U,V,W,X,Y,Z)

#and so, to automate all the system, I create this file!, feel free to look at it!
# Made By Teppi!


#Asking for input 
quit = ''

while quit != 'y':
  try:
  
    starting_number = int(input('What is the first NUMBER that you get? '))
    bookwork = int(input('How much bookwork you want to create? '))
    
  except ValueError:
    print('Only Integer ALLOWED!')
  
  else:
    #alphabet of bookwork
    word = 'abcdefghjklmnpqrsta'
    value = []
    
    print('')
    print('Here is the list of the future bookwork!')
  
   
    
    for i in range(bookwork):
      
    #giving the tens of the bookwork check to create letters and if statement  
      tens = (starting_number % 100) // 10
    
      if tens < 9:
        starting_number = starting_number + 10
    
    #Recheck the unit and tens to create letters
        tens = (starting_number % 100) // 10
        units = (starting_number % 10)
        
    #create letter by the sum of tenth digit and the unit
        tens_unit = tens + units
        letter = word[tens_unit]
    
    #Add the letter and the number as a string
        print(letter + str(starting_number))
    
      if tens == 9:
        
    #change unit to 1 and reset the tens collumm
        starting_number = starting_number - 89
    
    #Recheck the unit and tens to create letters
        tens = (starting_number % 100) // 10
        units = (starting_number % 10)
        
    #create letter by the sum of tenth digit and the unit
        tens_unit = tens + units
        letter = word[tens_unit]
        
    #print out the final answer with format of 00
        print(letter + str(f"{starting_number:02d}"))
  quit = input('Do you want to quit? (y/n) ')
  