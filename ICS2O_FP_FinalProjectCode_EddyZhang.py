#Name: Eddy Zhang
#Teacher: Ms.Katsman
#Course: ICS2O
#Date: January 22, 2019

#Final Project!

import random
import time

player1Name = input("What is your name? ")
while player1Name == "": #while the user does not enter anything for their name, the program will keep asking the user for their name
    player1Name = input("Please enter your name: ")
print("Hello", player1Name,"! Welcome to ICS2O Party!")
print("Each player starts off with 5 coins, and rolls a dice. \n\nIf you roll 1-3, you lose 3 coins, and if you roll 4-6, you gain 3 coins. \n\nAfter, you will answer a question! \n\nIf the answer is correct, you will get 5 coins, and if the answer is incorrect, you will lose 5 coins! \n\nTo win, you must collect stars. Each star costs 10 coins. \n\nAfter each round, you will get a chance to buy a star! \n\nWhoever has the most stars after 10 rounds will win! \n")
player1Ready = input("Enter anything when you are ready to roll the dice. ")

turns = 1
player1Coins = 5
player1Stars = 0
player1Turns = 1
player1Correct = 0
player1DiceTotal = 0
computerCoins = 5
computerStars = 0
computerTurns = 1
computerCorrect = 0
computerDiceTotal = 0
questionsIndex = 0
questions = [0,1,2,3,4,5,6,7,8,9]
questions = (random.sample(questions, 10))

while type(player1Ready) == str and turns <= 10: #while the user is ready and the user played less than or equal to ten turns, the game will run
    print("\nNow, it is round",turns,"!")
    while player1Turns == turns and computerTurns == turns: #this code will run when its the player 1's/computer's turn, which rolls the dice. It will run only once per turn
        diceRoll = random.randint(1,6)
        print("\nIt is your turn! Dice is rolling...")
        time.sleep(3)
        player1DiceTotal += diceRoll
        if diceRoll <= 3: #if the dice roll is less than/equal to 3, the player will lose 3 coins
            player1Coins -=3
            if player1Coins < 0: #if the user has no coins left, the player will have 0 coins
                player1Coins = 0
                print("You rolled a", diceRoll,"! You lost 3 coins! However, you cannot have less than 0 coins, therefore, you have", player1Coins, "coins.")
            else: #else, the user just lose 3 coins
                print("You rolled a", diceRoll,"! You lost 3 coins! Now you have", player1Coins, "coins.")
        else: #else, player wins 3 coins
            player1Coins += 3
            print("You rolled a", diceRoll,"! You gained 3 coins! Now you have", player1Coins, "coins.")
        player1Turns += 1
        diceRoll = random.randint(1,6)
        print("\nDice is rolling for your opponent...")
        time.sleep(3)
        computerDiceTotal += diceRoll
        if diceRoll <= 3: #if the dice roll is less than/equal to 3, computer will lose 3 coins
            computerCoins -=3
            if computerCoins < 0: #if the computer has no coins left, the computer will have 0 coins
                computerCoins = 0
                print("Your opponent rolled a", diceRoll,"! Your opponent lost 3 coins! However, your opponent cannot have less than 0 coins, therefore, your opponent has", computerCoins, "coins.")
            else: #else, the computer loses 3 coins
                print("Your opponent rolled a", diceRoll,"! Your opponent lost 3 coins! Now your opponent has", computerCoins, "coins.")
        else: #else, computer wins 3 coins
            computerCoins += 3
            print("Your opponent rolled a", diceRoll,"! Your opponent gained 3 coins! Now your opponent has", computerCoins, "coins.")
        computerTurns -= 1
        time.sleep(2)

    print("\nNow, you will answer a question! \n")
    time.sleep(2)
    print("Question",turns,":")
    if questions[questionsIndex] == 0: #if this is the question (0) that's next on the randomly generated order, this code will run
        print("Which data type is used to store numbers? \n a. int \n b. str \n c. boolean")
    elif questions[questionsIndex] == 1:#if this is the question (1) that's next on the randomly generated order, this code will run
        print("type(word1) \n<class ‘str’> \nWhat is saved in the variable word1? \n a. [‘computer’, ‘science’] \n b. “computer science is fun!” \n c. 1, 0, 1 \n d. True")
    elif questions[questionsIndex] == 2: #if this is the question (2) that's next on the randomly generated order, this code will run
        print("word2 = False, area = 25, perimeter = 50 \nType out the output of this code: (hint: think about booleen expressions, and capitals matter) \nprint(word2 and area != 25 or perimeter == 50)")
    elif questions[questionsIndex] == 3: #if this is the question (3) that's next on the randomly generated order, this code will run
        print("late = True \nmark = 40 \nif late and mark <50: \n\tprint(\"not good\") \nelse: \n\tprint(\"great\") \nIs this an example of a Compound Boolean Expression? (answer should be yes or no)")
    elif questions[questionsIndex] == 4: #if this is the question (4) that's next on the randomly generated order, this code will run
        print("print(12//5) \nWhat is the output of the code above? \n a. 5 \n b. 2.0 \n c. 2 \n d. \"DivisionError\"")
    elif questions[questionsIndex] == 5: #if this is the question (5) that's next on the randomly generated order, this code will run
        print("dataTypes = [\"strings\", \"integer\", \"lists\", \"float\"] \nprint(\"elements\" in dataTypes) \nWhat is the output of this code? (hint: think about booleen expressions, and capitals matter)")
    elif questions[questionsIndex] == 6: #if this is the question (6) that's next on the randomly generated order, this code will run
        print("Will the following code work? (answer should be either yes or no)\nnumbers = [1,2,3,4,5] \nprint(random.choice(numbers,6))")
    elif questions[questionsIndex] == 7: #if this is the question (7) that's next on the randomly generated order, this code will run
        print("What is the output of the following code? \nlistItems = [\"z\",5,\"b\",1] \nlistItems.sort() \nprint(listItems) \n a. [\"b\",\"z\",1,5] \n b. [1,\"b\",5,\"z\"] \n c. [1,5,\"b\",\"z\"] \n d. TypeError: unorderable types: int()<str()")
    elif questions[questionsIndex] == 8: #if this is the question (8) that's next on the randomly generated order, this code will run
        print("In the operation \"10.0//3\", is the answer a(n): \n a. int \n b. float \n c. str \n d. none of the above")
    else: #if this is the question (9) that's next on the randomly generated order, this code will run
        print("What is the data type of your answer for this question? \n a. str \n b. int \n c. float \n d. none of the above")
    userAnswer = input("Your Answer: ")
    userAnswerLower = (userAnswer.lower())
    possibleAnswers = ["a", "b", "c", "d", "true", "false", "yes", "no"]
    while userAnswer == "" or userAnswerLower not in possibleAnswers: #while the user does not provide an answer, the program will ask for an answer
        userAnswer = input("Please enter a valid answer: ")
        userAnswerLower = (userAnswer.lower())
    if questions[questionsIndex] !=2  and questions[questionsIndex] !=5: #if the question asked is not the third question (since the answer is case-sensitive), the answer is automatically lowercased
        userAnswer = (userAnswer.lower())
    questionAnswers = ["a", "b", "True", "yes", "c", "False", "no", "d", "b", "a"]
    if userAnswer == questionAnswers[questions[questionsIndex]]: #if the user got the right answer, they gain 5 coins
        player1Coins +=5
        player1Correct +=1
        print("Correct! You earned 5 coins! Now you have", player1Coins, "coins!")
    else: #else, they lose 5 coins
        player1Coins -= 5
        if player1Coins < 0: #if the user has no coins left, the player will have 0 coins
            player1Coins = 0
            print("Incorrect! You lost 5 coins! However, you cannot have less than 0 coins, therefore, you have", player1Coins, "coins.")
        else: #else, the user just loses 3 coins
            print("Incorrect! You lost 5 coins! Now you have", player1Coins,"coins.")
    time.sleep(2)

    chanceForStar = random.randint(0,1)
    if chanceForStar == 1: #if the random number is 1, then the player gets an oppotunity to get a star
        print("\nWow! Somehow, you have the opportunity to get a star!") 
        if player1Coins < 10: #if the user does not have enough coins to buy a star (less than 10 coins), then a message will appear and the user does not get a star
            print("But you do not have enough coins to buy a star.")
        else: #else, the player gains a star and loses 10 coins
            player1Stars +=1
            player1Coins -=10
            print("You got a star! \nNow, you have",player1Stars, "stars, and", player1Coins,"coins!")
    else: #else, the program will tell user that they do not have the chance to get a star
            print("\nYou do not have a chance to gain a star this turn. Better luck next time!")
    time.sleep(3)

    while computerTurns != turns: #while the computer didn't go yet, they will "answer" a question
        print("\nNow, your opponent will answer a question!")
        time.sleep(3)
        questionRightWrong = random.randint(0,1)
        if questionRightWrong == 1: #if the random number is a 1, then the computer gains 5 coins
            computerCoins +=5
            computerCorrect += 1
            print("Your opponent is correct! Your opponent earned 5 coins! Now your opponent has", computerCoins, "coins!")
        else: #if the random number is 0, then the computer loses 5 coins
            computerCoins -= 5
            if computerCoins < 0: #if the computer has no coins left, the player will have 0 coins
                computerCoins = 0
                print("Your opponent is incorrect! Your opponent lost 5 coins! However, your opponent cannot have less than 0 coins, therefore, your opponent has", computerCoins, "coins.")
            else: #else, the computer just loses 3 coins
                print("Your opponent is incorrect! Your opponent lost 5 coins! Now your opponent has", computerCoins,"coins.")
        computerTurns +=2
        time.sleep(3)
        chanceForStar = random.randint(0,1)
        if chanceForStar == 1: #if the random number is 1, then the computer gets an oppotunity to get a star
            print("\nWow! Somehow, your opponent has the opportunity to get a star!") 
            if computerCoins < 10: #if the computer does not have enough coins to buy a star (less than 10 coins), then a message will appear and the computer does not get a star
                print("But your opponent does not have enough coins to buy a star.")
            else: #else, the computer gains a star and loses 10 coins
                computerStars +=1
                computerCoins -=10
                print("Your opponent got a star! \nNow, your opponent has",computerStars, "stars, and",computerCoins,"coins!")
        else: #else, the program will tell the computer that they do not have the chance to get a star
            print("\nYour opponent does not have a chance to gain a star this turn. Better luck next time!")
        questionsIndex += 1
        turns += 1
        time.sleep(3)
        
    if turns <= 10: #if is it not the eighth turn already, the program will ask the user if they are ready
        player1Ready = input("\nEnter anything when you are ready for the next round. ")
    else: #if four turns have passed, the winner will be announced
        bonusAwards = 0
        while bonusAwards != 2: #if both bonus stars are not given out yet, this code will run until two bonus stars are given
            bonusAwards += 1
            if bonusAwards == 1: #if this is the first bonus star, this code will run
                print("\n10 rounds have passed, so it is time for... bonus stars! \nThis first star is for whoever got the most questions correct! \nThe star goes to...")
                time.sleep(3)
                if player1Correct > computerCorrect: #if user got more questions correct, this star goes to the user
                    userBonus = True
                else: #else, computer gets the star
                    userBonus = False
            else: #else, this code will run, which gives out the second bonus star
                print("The next bonus star is for whoever rolled the highest number in total over 10 rounds! The star goes to...")
                if player1DiceTotal > computerDiceTotal: #if user had a higher total, this star goes to the user
                    userBonus = True
                else: #else, computer gets the star
                    userBonus = False
            if userBonus == True: #if user beat the computer to get the bonus star, the user will get the bonus star
                time.sleep(3)
                player1Stars +=1
                print(player1Name,"! \nNow you have",player1Stars, "stars!")
            else: #else, computer will get the bonus star
                time.sleep(3)
                computerStars +=1
                print("Your opponent! \nNow your opponent has",computerStars, "stars!")
        print("The winner is...")
        time.sleep(1)
        if player1Stars > computerStars: #if user has more stars than the computer, user wins
             print("With",player1Stars,"stars,",player1Name,"wins!")
        elif player1Stars == computerStars: #if the amount of stars is equal, it is a tie
             print("It's a tie!")
        else: #if computer has more stars than the user, computer wins
            print("With",computerStars,"stars,","the computer wins!")

print("Goodbye!")
