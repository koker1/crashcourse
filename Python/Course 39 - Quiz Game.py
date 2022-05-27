# -----------------------------------------------------------------------
def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("---------------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A,B,C,D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    
    display_score(correct_guesses, guesses)

# -----------------------------------------------------------------------
def check_answer(answer, guess):
    
    if answer == guess:
        print("correct")
        return 1
    else:
        print("wrong")
        return 0 
# -----------------------------------------------------------------------
def display_score(correct_guesses, guesses):
    print("---------------------------------------")
    print("results")
    print("---------------------------------------")

    print("answers: ", end="")
    for i in questions:
        print(questions.get(i), end="")
    print()

    print("guesses: ", end="")
    for i in guesses:
        print(i, end="")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("your score is " +str(score)+"%")
# -----------------------------------------------------------------------
def play_again():
    
    response = input("Do you want to play again?: (yes or no): ")
    response = response.upper()

    if response == "yes":
        return True
    else:
        return False
# -----------------------------------------------------------------------


questions = {
    "Is hanjun gae?: ": "A",
    "Who created Minecraft?: ": "C",
    "Who is LMAO?: ": "A",
    "Who is your father?: ": "D"
}

options = [["A. True", "B. False", "C. No wonder", "D. Might be"],
          ["A. Steve", "B. Your mother", "C. Notch", "D. Obama"],
          ["A. Mao Ze Dong", "B. Winnie the Pooh", "C. Lil Pump", "D. Pewdiepie"],
          ["A. Iron Man", "B. Mr Beast", "C. President", "D. Darth Vader"]]

new_game()

while play_again():
    new_game()

print("cya")