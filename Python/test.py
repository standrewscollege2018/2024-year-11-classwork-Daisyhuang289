from random import randint

"""A function which tests whether the answers are correct, or invalid"""
def checkquestion(ques, correct, num):
    asked = 0
    check = True
    
    #Print out different strings, invalid input is entered
    if asked == 0:
        ans = input(f"Question {num}: {ques}\n").lower()
        
    else:
        ans = input().lower()
    
    #Check whether the answer is correct

        #If it is correct, return True
    if ans.strip() == correct.lower():
        print(f"{correct.lower()}{ans.strip()}")
        return True
        #Otherwise return False
    else:
        print(f"{correct.lower()}{ans.strip()}")
        return False

print("Welcome to the quiz!")

ask = True
#The question number
num_ques = 1
#The number of correct answerds
score = 0

#List of geography quiz questions and answers
geo = [["What is the capital of New Zealand?", "Wellington"], ["What is the capital of Brazil?", "Brasilia"], ["What is the capital of the USA?", "D.C. Washington"], ["What is the capital of Canada", "Ottawa"], ["What is the capital of Russia", "Moscow"], ["What is the capital of Japan", "Tokyo"], ["What is the capital of Australia?", "Canberra"], ["What is the capital of England?", "London"], ["What is the capital of China?", "Beijing"], ["What is the capital of South Korea", "Seoul"]]

#List of math quiz function
functions = ["-", "*", "+", "/"]

"""Ask for user's name repeatedly"""
name = input("\nEnter your name: ")
while ask == True:
    #If name is blank, name is not accepted
    if name.strip() == "":
        print("Cannot enter blank")
        name = input()
    #If it meets conditions, end loop
    else:
        ask = False

"""Repeatedly asking for the quiz wanted"""
quiz = input("\nWhat type of quiz would you like? (Maths or Geography) ")
while ask == False:
    #If quiz is blank, it is not accepted
    if quiz.strip() == "":
        print("Cannot enter blank")
        quiz = input()
        
    else:
        #Check what quiz the user wants
        if quiz.lower() == "maths":
            #Check whether num is a integer or string
            num = input("\nPlease chose how many questions you would like? ").strip()

            #Repeatedly ask for wanted num of questions
            while ask == False:
                #If num is blank, num is not accepted
                if num.strip() == "":
                    print("Cannot enter blank")
                    num = input()
                
                #Check whether num is a string or integer
                try:
                    num_int = int(num)
                    ask = True
                except ValueError:
                    print("Please enter a number")
                    num = input()
                    
        elif quiz.lower() == "geography":
            num_int = len(geo)
            ask = True
            
        #If it doesn't exist, it is not accepted
        else:
            print("This is not a valid quiz")
            quiz = input()

"""Repeatedly ask for their guess of how many correct answers"""
guess = input(f"\nHi {name.capitalize()}, there will be {num_int} questions in this quiz. How many do you think you will get correct? ")
while ask == True:
    #Checking whether the input is a integer or not
    try:
        guess = int(guess)
        
        #Checks whether the number is lower than 0
        if guess < 0:
            print("Please enter a number 0 or higher")
            guess = input()

        #Check whether the number is higher than the number of questions
        if guess > num_int:
            print(f"Please enter a number {num_int} or lower")
            guess = input()
            
        #If all conditions are met, end loop
        else:
            ask = False
            
    except ValueError:
        print("Please enter a integer")
        guess = input()
        
print("\nOkay, good luck!\n")

"""Start quiz"""

#Geography quiz
if quiz == "geography":
    for i in geo:
        checkquestion(i[0], i[1], num_ques)
        if checkquestion==True:
            print("That's right!")
            score += 1
        elif False:
            print(f"Sorry, that's wrong. The answer is {i[1]}")
        num_ques += 1

#Maths quiz
elif quiz  == "maths":
    for i in range(num_int):
        #Pick random questions, with random numbers and functions
        number1 = randint(0, 100)
        number2 = randint(0, 100)
        process = randint(0, len(functions)-1)

        #Print the questions and figure the answers
        while ask == False:
            if process == 0:
                value = number1 - number2
            elif process == 1:
                value = number1 * number2
            elif process == 2:
                value = number1 + number2
            elif process == 3:
                value = number1/number2
            answer = input(f"{num_ques}. {number1} {functions[process]} {number2} = ")
            if answer.strip()== "":
                print("Cannot enter blank")
                answer = input()
            else:
                ask = True
        #Check whether entered answer is a float or not
        try:
            float_ans = float(answer)
            #If it is equal to the calculated answer, its right
            if float_ans == value:
                print("That's right!")
                score += 1
        except ValueError:
            print(f"Sorry, that's wrong. The answer is {value}")
        num_ques += 1
#Check whether the score is over, below, or equal to the guess
if guess > score:
    diff = "less than"
elif guess < score:
    diff = "more than"
else:
    diff = "equal to"

#Print score, and whether you passed your estimate
print(f"You got {score} questions correct. That's {diff} your goal of {guess}.")
print("Goodbye!")
