print("welcome to the game!")

startGame = input("Do you want to start the quiz? ")

if startGame.lower() != "yes":
    quit()

print("Okay! Lets start!")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("You are correct!")
    score += 1
else:
    print("You are incorrect!")

answer = input(" What does RAM stand for? ")
if answer.lower() == "random access memory ":
    print("You are correct!")
    score += 1
else:
    print("You are incorrect!")

answer = input("What does ROM stand for? ")
if answer.lower() == "read only memory":
    print()
    score += 1
else:
    print("You are incorrect!")

answer = input("What does ALU stand for? ")
if answer.lower() == "arithmetic logic unit":
    print()
    score += 1
else:
    print("You are incorrect")

answer = input("What does CAD stand for? ")
if answer.lower() == "computer aided design":
    print()
    score += 1
else:
    print("You are incorrect")
answer = input("What does DVD stand for? ")
if answer.lower() == "digital versatile disk":
    print()
    score += 1
else:
    print("You are incorrect")

print("You got " + str(score) + " correct!")
