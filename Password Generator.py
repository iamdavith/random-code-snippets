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
     |    1. Digits
     |    2. Lowercase letters
     |    3. Uppercase letters  
     |    4. Special characters
     |    5. All of the above (+ exit)  
     |    6. Exit''')
 
     characterList = ""
 
     while(True):
         choice = int(input("Pick a number: "))
         if(choice == 1):
             
             characterList += string.digits
         elif(choice == 2):
         
             characterList += string.ascii_lowercase
         elif(choice == 3):
        
             characterList += string.ascii_uppercase
         elif(choice == 4):
         
             characterList += string.punctuation
         elif(choice == 5):
             characterList += string.digits
             characterList += string.ascii_lowercase
             characterList += string.ascii_uppercase
             characterList += string.punctuation
             break
         elif(choice == 6):
             break
         else:
             print("Please pick a valid option!")
 
     password = []
 
     for i in range(length):
  
         randomchar = random.choice(characterList)
     
         password.append(randomchar)
     print('''Your password is: 
     |    ''' + "".join(password))


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
