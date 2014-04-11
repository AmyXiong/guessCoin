#! usr/bin/env python
import random

f = open("highScore.txt", "r+")
highScore = f.read()
highScore = int(highScore)
score = 0

print "Coin Guessing Game.  All time high score: %d correct" %(highScore)

while True: 
	guess = raw_input("Predict heads or tails> ")

	coin = random.randint(1,2)

	if coin == 1:
		result = "Heads"
	else:
		result = "Tails"

	if guess == result:
		score = score + 1
		print "It is", result, "Your score is: ", score
	else: 
		print "It is", result, "Game over."
		f.seek(0)
		if score > highScore:
			f.truncate()
			score = str(score)
			f.write(score)
			highScore = score
		break
	
print "Your Score: %s\n" %(score)
print "High Score: %s\n" %(highScore)