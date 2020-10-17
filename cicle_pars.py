# Python3 program for the above approach 

# Function for finding the temperature 
def findTemperature(x, y, s): 

	# Store Day1 - Day2 in diff 
	diff = (x - y) * 6
	Day2 = (diff + s) // 2

	# Remaining from s will be Day1 
	Day1 = s - Day2 

	# Print Day1 and Day2 
	print("Day1 : ", Day1) 
	print("Day2 : ", Day2) 

# Driver Code 
if __name__ == '__main__': 
	x = 5
	y = 10
	s = 40

	# Functions 
	findTemperature(x, y, s) 

# This code is contributed by Mohit Kumar

