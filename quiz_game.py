print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

# Add questions here.
answer = input("#? ")
# Add answers here.
if answer.lower == "#":
    print('Correct!')
    score += 1
else:
    ('Incorrect!')

answer = input("#? ")
if answer.lower == "#":
    print('Correct!')
    score += 1
else:
    ('Incorrect!')

answer = input("#? ")
if answer.lower == "#":
    print('Correct!')
    score += 1
else:
    ('Incorrect!')

answer = input("#? ")
if answer.lower == "#":
    print('Correct!')
    score += 1
else:
    ('Incorrect!')

answer = input("#? ")
if answer.lower == "#":
    print('Correct!')
    score += 1
else:
    ('Incorrect!')

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
