print("*****WELCOME*****")
print("Your answer should be in only Capital ")
name= input("Enter your name\t")
print(name,"All the best")
print("Q1. What is the capital of France?\nA) Berlin\nB) Madrid\nC) Paris\nD) Rome\n")
answer1=input()
if answer1=='C':
    print("Correct")
else:
    print("Wrong")
print("Q2. Which planet is known as the Red Planet?A) Earth\nB) Mars\nC) Jupiter\nD) Venus\n")
answer2=input()
if answer2=='B':
    print("Correct")
else:
    print("Wrong")
print("Q3. What is the largest mammal in the world?A) African Elephant\nB) Blue Whale\nC) Giraffe\nD) Great White Shark\n")
answer3=input()
if answer3=='B':
    print("Correct")
else:
    print("Wrong")

if answer1=='C' and answer2=="B" and answer3=='B':
    print("Your Score is 300")
elif answer1=='C'and answer2=="B" and answer3!='B':
    print("Your Score is 200")
elif answer1=='C'and answer2!="B" and answer3=='B':
    print("Your Score is 200")
elif answer1!='C'and answer2=="B" and answer3=='B':
    print("Your Score is 200")
elif answer1=='C'and answer2!="B" and answer3!='B':
    print("Your Score is 100")
elif answer1!='C'and answer2=="B" and answer3!='B':
    print("Your Score is 100")
elif answer1!='C'and answer2!="B" and answer3=='B':
    print("Your Score is 100")
else:
    print("Your Score Nothing")