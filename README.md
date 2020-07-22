# Hangman

HANGMAN
Run the script to play hangman game. 
The game takes input from the user in the form of ASCII lower case letter. 
The user has eight lives and a wrong attempt leads to losing a life.
Typing more than one letter, or a letter that is not ASCII lower case or typing a letter that has previously been typed in the same game - are considered as Errors.
Errors do not lead to losing a life. Wrong attempts - however are calculated as losing a life.

H A N G M A N
Type "play" to play the game, "exit" to quit: > play

----------
Input a letter: > a

-a-a------
Input a letter: > i

-a-a---i--
Input a letter: > o
No such letter in the word

-a-a---i--
Input a letter: > o
You already typed this letter

-a-a---i--
Input a letter: > p

-a-a---ip-
Input a letter: > p
You already typed this letter

-a-a---ip-
Input a letter: > h
No such letter in the word

-a-a---ip-
Input a letter: > k
No such letter in the word

-a-a---ip-
Input a letter: > a
You already typed this letter

-a-a---ip-
Input a letter: > z
No such letter in the word

-a-a---ipt
Input a letter: > t

-a-a---ipt
Input a letter: > x
No such letter in the word

-a-a---ipt
Input a letter: > b
No such letter in the word

-a-a---ipt
Input a letter: > d
No such letter in the word

-a-a---ipt
Input a letter: > w
No such letter in the word
You are hanged!

Type "play" to play the game, "exit" to quit: > exit
