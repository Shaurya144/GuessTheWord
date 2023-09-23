import random

def generateWord():

  with open("dictionary.txt", "r") as file:

    Word_List = file.readlines()

  difficulty = input("What difficulty do you want to play? Easy (E), Medium (M), or Hard (H)? ").lower()

  # User Difficutly
  while difficulty not in ["e","m","h"]:
    difficulty = input("What difficulty do you want to play? Easy (E), Medium (M), or Hard (H)? ").lower()

  while True:
    randomIndex = random.randint(0, len(Word_List) - 1)
    randomChoice = Word_List[randomIndex].strip().lower()

    if difficulty == "e" and len(randomChoice) <= 5:
      break
    elif difficulty == "m" and len(randomChoice) <= 10 and len(randomChoice) > 5:
      break
    elif difficulty == "h" and len(randomChoice) >= 11:
      break

  return randomChoice

def generateletters(word, lettersToReveal, lettersGuessed):

  obfuscated = ""

  for letter in word:

    # If the letter has been guessed, show it
    if letter in lettersToReveal:
      obfuscated += (letter + " ")

    # Otherwise, show the hyphen
    else:
      obfuscated += "_ "

  # Join the list into a space-separated string so it can be displayed
  alreadyGuessed = " ".join(lettersGuessed)

  # Only show the letters incorrectly guessed if there are some!
  if len(alreadyGuessed) == 0:
    return obfuscated + "\n"
  else:
    return obfuscated+"\tAlready guessed: "+alreadyGuessed+"\n"

# This function builds up the Snowman depending on how many guesses were made
def generate_snowman(guesses):
    
  snowman = []

  if guesses >= 1:
    bottomSnowball = "  (       )" + "\n" +"   \'-----\'" # /n = new line
    snowman.append(bottomSnowball)

  if guesses >= 2:
    middleSnowball = "   (     )"
    snowman.insert(0,middleSnowball)
          
  if guesses >= 3:

    headSnowball = "    (   )"
    snowman.insert(0,headSnowball)

  if guesses >= 4:
    snowman[0] = "    (--__--)"

  if guesses >= 5:
    snowman[1] = "--<(  .  )>--"
    snowman[2] = "  (   .   )" + "\n" + "   \'-----\'"

  if guesses >= 6:

    topHat = "     ___" + "\n" + "   _|___|_"
    snowman.insert(0,topHat)

  # Returns a string
  return "\n".join(snowman)

print("Welcome to Snowball!\n")

# Random Word from text file
word = generateWord()

print("\nLet's get started...\n")

print(generateletters(word, "", []))

tries = 0
guessedWrong = []
guessedCorrect = []

while tries < 6:

  guess = input("Make a guess: ").lower()

  while guess in guessedWrong or guess in guessedCorrect:
    guess = input("You guessed that before. Make another guess: ").lower()

  while guess.isalpha() == False:
    guess = input("You input must be a letter or word. Make another guess: ")
  
  if guess not in word:

    if len(guess) == 1:
      guessedWrong.append(guess)
      
    tries += 1
    
  else:

    if guess == word:
      print("You've won!")
      break
    else:
      guessedCorrect.append(guess)

  lettersToShow = generateletters(word, guessedCorrect, guessedWrong)

  # Before displaying text - check to see if the user has won
  if "_" not in lettersToShow:
    print(lettersToShow)
    print("You've won!")
    break
  else:
    # If the user hasn't won, show the display
    print(lettersToShow)
    print(generate_snowman(tries))

else:
  # When the tries run out, the user has lost
  print("You lose. The word was \""+word + "\".")
  
print("Thanks for playing!") 