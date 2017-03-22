# takes list of numbers and prints out *

def draw_stars(arr):


	for x in arr:
		print "*" * x

num = [4, 6, 1, 3, 5, 7, 25]

draw_stars(num)


# When interger is passed, prints out *. When a string is passed, display first letter of the string. 

def draw_stars_again(arr):

	for x in arr:
		if isinstance(x, int):
			print "*" * x

		elif isinstance(x, str):
			length = len(x)
			first = x[0].lower()
			print length * first

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

draw_stars_again(x)