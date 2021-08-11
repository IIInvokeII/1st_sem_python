import random

HANGMAN_PICS = ['''
    +---+
         |
         |
         |
         |
         |
        ===''',
                '''
    +---+
    |    |
         |
         |
         |
         |
        ===''',
                '''
    +---+
    |    |
    |    |
         |
         |
         |
        ===''','''
    +---+
    |   |
    |   |
    O  |
        |
        |
       ===''', '''
    +---+
    |   |
    |   |
    O  |
    |   |
        |
       ===''', '''
    +---+
    |    |
    |    |
    O   |
   /|   |
         |
       ===''', '''
    +---+
    |    |
    |    |
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    |    |
    |    |
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    |    |
    |    |
    O   |
   /|\  |
   / \  |
       ===''']

f=open("hangman.txt","r")
w=f.read()
f.close()
words=w.split()

def getRandomWord(wordList):
    """
    Returns a random string from the passed list of strings.
    """
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print()
    print(HANGMAN_PICS[len(missedLetters)])

    print()
    print('Missed letters: ', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')

    print()
    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end =' ')
    print()

def getGuess(alreadyGuessed):
    """
    Returns the letter the player entered.
    Ensures the player enters a single letter and nothing else.
    """
    while True:
        print('Please guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Only a single letter is allowed.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a letter from the alphabet.')
        else:
            return guess

def playAgain():
    """
    Returns True if the player wants to play again, False otherwise.
    """
    print('Would you like to play again? (y)es or (n)o')
    return input().lower().startswith('y')

print('|_H_A_N_G_M_A_N_|')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False


while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('You guessed it!')
            print('The secret word is "' + secretWord + '"! You win!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess


        if len(missedLetters) == len(HANGMAN_PICS) -1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
