secret_word = "giraffe"
guess = ""
guess_limit = 3
guess_count = 0
Out_of_guesses = False
while guess != secret_word and not Out_of_guesses:
    if guess_count < guess_limit:
        guess = input("enter guess")
        guess_count += 1
    else:
        Out_of_guesses = True
    if Out_of_guesses:
        print("out of guesses you loose!")
    else:
        print("You win!")








