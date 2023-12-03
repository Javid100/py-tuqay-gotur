score = 0
ask= str(input("Hello, You are in Python Quiz. Your quiz started now. What is your name? : "))

    

while True:
    print("Options:")
    print("1. Help")
    print("2. Start Quiz")
    print("3. End Quiz")
    print("4. Leaderboard")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("Help: This program is a quiz game. You can start the quiz, view the leaderboard, or quit.")
    elif choice == "2":
        f = open("questions.txt", "r")
        a = open("answers.txt", "r")          
                
        for j in range(10):
            for i in range(6):
                print(f.readline(), end="")
            ans = str(input("Write your answer (For example (A): "))
            if ans == a.readline().strip():
                    score += 1
                    print("True")
            else:
                    print("False")
        try:  
            percentage = (score *100)/10
        except ZeroDivisionError:
            print('0% quetions are correct')

        print(f'{percentage}% questions are correct.')
        f.close()
        f = open("leadboard.txt", "w")
        f.write(f"{ask} {percentage}")
        f.close()

    elif choice == "3":
        print("Goodbye! Thanks for playing.")
        break
    elif choice == "4":
        f = open("leadboard.txt", "r")
        print(f.read())