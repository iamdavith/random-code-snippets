import string
import random
import sys

def generate():
     
     length = int(input('''Enter password length:
1-5: weak
6-9: good
10+: strong
'''))
 
     print('''Choose character set #s: 
         1. Digits
         2. Letters
         3. Special characters
         4. Exit''')
 
     characterList = ""
 
     while(True):
         choice = int(input("Pick a number: "))
         if(choice == 1):
         
             characterList += string.digits
         elif(choice == 2):
        
             characterList += string.ascii_letters
         elif(choice == 3):
         
             characterList += string.punctuation
         elif(choice == 4):
             break
         else:
             print("Please pick a valid option!")
 
     password = []
 
     for i in range(length):
  
         randomchar = random.choice(characterList)
     
         password.append(randomchar)
     print('''Your password is: 
     ''' + "".join(password))


def cycle():
    q = str(input('''Generate again?
Warning: not generating again will terminate the program
Y/N? '''))
    pr = "y"
    if q.lower() == pr:
        generate()
        cycle()
    else:
       sys.exit()

     
generate()    
cycle()