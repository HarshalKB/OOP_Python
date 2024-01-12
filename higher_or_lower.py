import random

# Card constants
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

N_CARDS = 10

def getCard(deckList):
    return deckList.pop()

def shuffle(deckList):
    deckListOut = deckList.copy()
    random.shuffle(deckListOut)
    return deckListOut

print('Welcome to Higher or Lower')
print('Choose whether the next card has higher rank or lower rank than the current card')
print('Getting it right adds 20 points, getting it wrong loses 15 points')
print('You have 50 points to start with')
print()

startingDeck = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank': rank, 'suit': suit, 'value': thisValue + 1}
        startingDeck.append(cardDict)

score = 50

while True:
    print()
    gameDeck = shuffle(startingDeck)
    currentCard = getCard(gameDeck)
    currCardRank = currentCard['rank']
    currCardValue = currentCard['value']
    currCardSuit = currentCard['suit']
    print(f'Starting card is: {currCardRank} of {currCardSuit}.')
    print()

    for cardNumber in range(N_CARDS):
        answer = input('Will the next card be higher or lower: ("h" for higher, "l" for lower) ')
        answer = answer.casefold()

        nextCard = getCard(gameDeck)
        nextCardRank = nextCard['rank']
        nextCardSuit = nextCard['suit']
        nextCardValue = nextCard['value']

        print(f'Next card is {nextCardRank} of {nextCardSuit}')

        if answer == 'h':
            if nextCardValue > currCardValue:
                print('You got it right, it was higher')
                score += 20
            else:
                print('Sorry it was not higher')
                score -= 15

        elif answer == 'l':
            if nextCardValue < currCardValue:
                print('You got it right, it was lower')
                score += 20
            else:
                print('Sorry it was not lower')
                score -= 15
        else:
            print('Incorrect entry, restart the game.')
            break

        print(f'Your score is: {score}')
        print()
        currentCard = nextCard
        currCardValue = nextCardValue

    goAgain = input('To play again, press ENTER, or "q" to quit: ')
    if goAgain == 'q':
        break

print('OK Bye')