# Python Quiz Game
#Using the end and sep arguments to create a prompt before taking the quiz.
print("Welcome to Max's quiz ", end = '')
print(",are you ready? ", sep= '')

def main():
    keepLooping = True
    while keepLooping:
        try:
            print("""
            1: Movies
            2: Music""")
            print("Press 0 to end the quiz.")
            print("Press 3 to see more.")
            choice = int(input("Which quiz would you like to take?(1 or 2): "))
        except:
            print("Invalid selection. Try again.")
        else:
            if (choice == 1):
                movie_quiz()
            elif (choice == 2):
                music_quiz()
            elif (choice == 0):
                keepLooping = False
            else:
                print("Invalid selection. Try again.")

                
def movie_quiz():
    questions = ("What pill does Neo take in The Matrix?: ",
                 "What are the names of the two spys on the new movie "
                                                    "Bullet Train?: ",
                 "What house was Harry Potter in?: ",
                 "From what classic thriller does Robert De Niro say "
                                                    "'You talkin' to me?'?",
                 "Who plays the joker in the 2008 Batman film titled,"
                                                    " The Dark Knight")

    options = (("A. Red", "B. Yellow", "C. Blue", "D. Green"),
               ("A. Coconut/Pear", "B. Lemon/Tangerine", "C. Ruff/Tuff",
                                                    "D. Orange/apple"),
               ("A. Hufflepuff", "B. Ravenclaw", "C. Gryffindor", "D. Slytherin"),
               ("A. Taxi Driver", "B. Goodfellas", "C. The Godfather",
                                                   "D. A Bronx Tale"),
               ("A. Joaquin Phoenix", "B. Heath Ledger", "C. Jack Nicholson",
                                                    "D. Cameron Monaghan"))

    answers = ("A", "B", "C", "A", "B")
    guesses = []
    score = 0
    question_num = 0

    for question in questions:
        print("---------------------")
        print(question)
        for option in options[question_num]:
            print(option)

        guess = input("Enter (A, B, C, D): ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print("Correct!")
        elif guess == "0"
            quit()
        else:
            print("Incorrect")
            print(f"{answers[question_num]} is the correct answer")
        question_num += 1

    print("-----------------------")
    print("      Results!         ")
    print("-----------------------")

    print("Answers: ", end="")
    for answer in answers:
        print(answer, end=" ")
    print()

    print("Guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()

    score = int(score / len(questions) * 100)
    print(f"Your score is: {score}%")

def music_quiz():
    questions = ("What singer has a Billboard no.1 every December?: ",
                 "8 Mile is named after a road in which city?: ",
                 "Which classical composer was deaf?: ",
                 "Which Marvel movie's soundtrack won two Grammys? ",
                 "What was Elvis Presley’s first hit in 1956?")

    options = (("A. Drake", "B. Taylor swift", "C. Mariah Carey", "D. Jay-Z"),
               ("A. Fort Myers", "B. Detroit", "C. Atlanta", "D. Wynwood"),
               ("A. Ludwig Van Beethoven", "B. Wolfgang Amadeus Mozart",
                "C. Johann Sebastian Bach", "D. Antonio Vivaldi"),
               ("A. Iron Man", "B. Ant Man", "C. Avengers",
                "D. Black Panther"),
               ("A. All Shook Up", "B. Jailhouse Rock", "C. It’s Now Or Never",
                                                    "D. Heartbreak Hotel"))

    answers = ("C", "B", "A", "D", "D")
    guesses = []
    score = 0
    question_num = 0

    for question in questions:
        print("---------------------")
        print(question)
        for option in options[question_num]:
            print(option)

        guess = input("Enter (A, B, C, D): ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print("Correct!")
        elif guess == "0"
            quit()
        else:
            print("Incorrect")
            print(f"{answers[question_num]} is the correct answer")
        question_num += 1

    print("-----------------------")
    print("      Results!         ")
    print("-----------------------")

    print("Answers: ", end="")
    for answer in answers:
        print(answer, end=" ")
    print()

    print("Guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()

    score = int(score / len(questions) * 100)
    print(f"Your score is: {score}%")

def more():
    x = 1
    y = 2
    # The != operator is the not equal operator
    print(x != y)

    # The <,>,<=,>= operators are less or greater than and equals to.
    print(x > y)

    # The * operator is used for multiplication
    print(10 * 10)

    # The ** operator is the exponent operator.
    print(5 ** 2)

    # The / operator is used for division.
    print(10 / 2)

    # The - operator is used for subtraction
    print(10 - 3)

    # The % operator is the modulo operator used to calculate the remainder
    print(5 % 2)

    # The // operator is used for floor division
    print(10 // 3)

    # The not operator is a boolean which comes to be either true or false.
    print(not 0)

    # The and operator is a boolean which

main()


