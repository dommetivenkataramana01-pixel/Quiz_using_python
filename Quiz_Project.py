#IN THIS PROJECT WE ARE GOING DO A QUIZE GAME BY USING PYHON
marks=10
print("Welcome to the computer quiz!")
playing=input("Do you want to play the quiz?: ").lower()
if(playing!="yes"):
    print("No worries! Come back anytime you want to play")
    quit()
print("Okay! Let's play the quiz:- ")
#1 question
answer=input("What does the CPU stand for: ").lower()
if(answer=="central processing unit"):
    print("Correct!!")
else:
    print("Incorrect!!")
    marks=marks-1
#2 question
answer=input("What does RAM stand for?: ").lower()
if(answer=="random access memory"):
    print("Correct!!")
else:
    print("Incorrect!!")
    marks=marks-1
#3 question
answer=input("What does the acronym URL stand for?: ").lower()
if(answer=="uniform resource locator"):
    print("Correct!!")
else:
    print("Incorrect!!")
    marks=marks-1
#4 question
answer=input("What does GPU stand for?: ").lower()
if(answer=="graphics processing unit"):
    print("Correct!!")
else:
    print("Incorrect!!")
    marks=marks-1
#5 question
answer=input("What is the brain of the computer called?: ").lower()
if(answer=="cpu"):
    print("Correct!!")
else:
    print("Incorrect!!")
    marks=marks-1
#6 question
answer=input("What does HTML stand for?: ").lower()
if(answer=="hypertext markup language"):
    print("Correct!!")
else:
    print("Incorrect!!")
    marks=marks-1
#7 question
answer=input("What does OS stand for?: ").lower()
if(answer=="operating system"):
    print("Correct!!")
else:
    print("Incorrect!!")
    marks=marks-1
#8 question
answer=input("What does the acronym WWW stand for?: ").lower()
if(answer=="world wide web"):
    print("Correct!!")
else:
    print("Incorrect!!")
    marks=marks-1
#9 question
answer=input("What does LAN stand for?: ").lower()
if(answer=="local area network"):
    print("Correct!!")
else:
    print("Incorrect!!")
    marks=marks-1
#10 question
answer=input("What does IP stand for (as in IP address)?: ").lower()
if(answer=="internet protocol"):
    print("Correct!!")
else:
    print("Incorrect!!")
    marks=marks-1
    
print("Your final marks are:", marks)

if(marks==10):
    print("Great! You got a perfect score!")
elif(marks<10 and marks>7):
    print("Good job!")
elif(marks<=7 and marks>4):
    print("Not bad, keep practicing!")
else:
    print("You need to study more!")


