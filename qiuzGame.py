print("Welcome to python quiz! ")

playing = input('Do you want to play? ')

if playing.lower() != "yes":
    quit()

print("Okay, Let's play :) ")

score = 1

#Question 1
answer = input("Which symbol is used for writing comments in python? ")

if answer.lower() == '#':
    print("Correct!")
    score+=1
else:
    print("Incorrect!\n")

#Question 2
answer = input("""What will be the value of the following Python expression? 
               
4 + 3 % 5 \n""")

if answer.lower() == '7':
    print("Correct!")
    score+=1
else:
    print("Incorrect!\n")

#Question 3
answer = input("What is the correct file extension for Python files? ")

if answer.lower() == '.py':
    print("Correct!")
    score+=1
else:
    print("Incorrect!\n")

#Question 4
answer = input("""Which of the following is used to define a block of code in Python language? 

a : Indentation
b : Key
c : Brackets \n""")
               

if answer.lower() == 'a':
    print("Correct!")
    score+=1
else:
    print("Incorrect!\n")

#Question 5
answer = input("""Which keyword is used for function in Python language? 

a : def
b : fun
c : define \n""")

if answer.lower() == 'a':
    print("Correct!")
    score+=1
else:
    print("Incorrect!\n")

#Question 6
answer = input("""What does pip stand for python? 

a : Pip Installs Python
b : Pip Installs Packages
c : Preferred Installer Program /n""")

if answer.lower() == 'c':
    print("Correct!")
    score+=1
else:
    print("Incorrect!\n")

#Question 7
answer = input("Which is the truncation division operator in Python? ")

if answer.lower() == '//':
    print("Correct!")
    score+=1
else:
    print("Incorrect!\n")

#Question 8
answer = input("""Which of the following is not a core data type in Python programming? 

a : Tuples
b : List
c : Class \n""")

if answer.lower() == 'c':
    print("Correct!")
    score+=1
else:
    print("Incorrect!\n")

#Question 9
answer = input("""Which one of the following is not a keyword in Python language? 

a : pass
b : evert
c : assert
d : non local \n""")

if answer.lower() == 'b':
    print("Correct!")
    score+=1
else:
    print("Incorrect!\n")

#Question 10
answer = input("""Which of the following statements is used to create an empty set in Python? 

a : ()
b : []
c : set() \n""")

if answer.lower() == 'c':
    print("Correct!")
    score+=1
else:
    print("Incorrect!\n")

print("You got " + str(score) + " questions correct!\n")

print("You got " + str((score/10)*100) + " %.")