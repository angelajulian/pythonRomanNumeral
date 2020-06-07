
rDict = {
'I':1, 
'V':5, 
'X':10, 
'L':50, 
'C':100, 
'D':500, 
'M':1000
}

# make exposed user strings easier to find/edit
initialMessage = "Enter the number you want translated. Limit between 1-9999:"
numberHigh = "Please enter a number between 1-9999"
noZero = "The Romans did not have the concept of Zero!"
notRoman = "This is not a roman numeral. Please enter an interger >= 9999 OR a string including up to 21 characters from the following list: I, V, X, L, C, D, and/or M"
fewer = "Please enter fewer than 21 characters"

def sanitizeInput(userInput):
	try: 
		userInput = int(userInput)
		if (userInput==0):
			print(noZero) 
			return
		print(ToRomanNums(userInput))
	except: 
		if (userInput is ''): 
			print(noZero)
			return
		# sanitize user input
		nums = userInput.upper()
		nums = list(nums)

		toRoman = True

		# check that the number entered is not too large; the longest roman numeral under 5000 is 16 characters long
		if len(nums) > 21: 
			print(fewer)
			# quit if number does not conform to requirements
			return

		if Roman(nums): 
			print(romanTranslator(translateList(nums)))
			return
		else: 
			print(notRoman)

			 

def ToRomanNums(num):
	print("Got to RomanNums")
	romanNumeral = ''
	ValueDict = sorted(rDict.items(), key=lambda x: x[1], reverse=True)
	# if the number is divisible by the dictionary value, replace with dictionary key * how much it's divisible by
	i = 0
	while i < len(ValueDict):
		pair = ValueDict[i]
		mult = num/pair[1]
		if (mult > 0): 
			romanNumeral = romanNumeral + (pair[0] *  mult)
			num = num%pair[1]
		#TODO: how to handle 9s? 
		i +=1 

	return(romanNumeral)



def Roman(nums): 
	# TODO: need something to ensure users don't use V, L or D to reduce the number
	# check if all char are roman numerals
	fromRoman = True
	for num in nums:
		if num in rDict: 
			fromRoman *= True
		else:
			fromRoman *= False
	return fromRoman


def translateList(userList):
	# replaces all items in list with ints from rDict
	for i, item in enumerate(userList):
		userList[i] = rDict[item]
	return userList


def romanTranslator(userInput): 
	# after translating list
	# if the input passes sanitation only
	total = 0
	length = len(userInput)
	i = 0 

	while i < length: 
		if i == (length - 1): 
			total += userInput[i]
		# roman numerals only have 1 charcter less: ex 8 is VIII rather than IIX
		elif (userInput[i] < userInput[(i+1)]):
			total -= userInput[i]
		else: 
			total += userInput[i]
		i+=1

	return(total)


	 


userInput = raw_input(initialMessage)
sanitizeInput(userInput)
