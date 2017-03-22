import random

def coinToss(flip):

	count = 1
	head_count =0
	tail_count = 0


	for x in range (0,flip):	
		toss=random.randint(0,1)

		if toss == 1:
			head_count +=1
			print "Attempt #", count, ": Throwing a coin... It's a head! ...Got ", head_count, "head(s) so far and ", tail_count, "tail(s) so far"
		
		else: 
			tail_count +=1
			print "Attempt #", count, ": Throwing a coin... It's a tail! ...Got ", head_count, "head(s) so far and ", tail_count, "tail(s) so far"

		count +=1

	print "Ending the program, thank you!"

coinToss(5000)

