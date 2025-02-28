from random import choice

playerChoose = int(input("What do you choose? Type '0' for Rock, '1' for Paper or '2' for Scissors.\n"))
computerOptions = [0, 1, 2]
computerChoose = choice(computerOptions)

def numberToLetter(choose):
    if choose == 0:
        return "rock"
    elif choose == 1:
        return "paper"
    else:
        return "scissor"

if playerChoose == computerChoose:
    result = "tied the game"
elif playerChoose == 0 and computerChoose == 2:
    result = "win"
elif playerChoose == 2 and computerChoose == 0:
    result = "lose"
elif playerChoose > computerChoose:
    result = "win"
elif playerChoose < computerChoose:
    result = "lose"

print(f'''You choose {numberToLetter(playerChoose)}
Computer choose {numberToLetter(computerChoose)}
You {result}
''')
