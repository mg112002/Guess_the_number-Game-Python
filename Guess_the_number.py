n = 0
g = 9
while n != 18:
    print("Guesses left =", g)
    n = int(input("Guess the number-"))
    g -= 1
    if g == 0:
        print("No guesses left\n", "-----GAME OVER-----")
        break
    elif n > 18:
        print("The number entered is greater than the hidden number")
    elif n < 18:
        print("The number entered is smaller than the hidden number")
    else:
        print("Woohooo!! You have guessed the correct number\n", "-----;)You Win-----")
        break
