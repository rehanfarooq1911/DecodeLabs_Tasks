def main():
    score = 0   

    print("Welcome to the General Knowledge Quiz!")
    print("Answer the 3 questions below.\n")

    answer = input("Q1. What is the capital of France? ")   
    answer = answer.strip().lower()                          
    if answer == "paris":                                    
        print("Correct! +1 point\n")                         
        score += 1
    else:
        print("Wrong! The correct answer is Paris.\n")

    answer = input("Q2. Which planet is known as the Red Planet? ")
    answer = answer.strip().lower()
    if answer == "mars":
        print("Correct! +1 point\n")
        score += 1
    else:
        print("Wrong! The correct answer is Mars.\n")

    answer = input("Q3. How many continents are there on Earth? ")
    answer = answer.strip().lower()
    if answer == "7" or answer == "seven":
        print("Correct! +1 point\n")
        score += 1
    else:
        print("Wrong! The correct answer is 7.\n")

    print("----- Quiz Complete -----")
    print(f"Your final score: {score}/3")


if __name__ == "__main__":
    main()