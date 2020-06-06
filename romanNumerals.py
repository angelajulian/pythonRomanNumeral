
rDict = {
'I':1, 
'V':5, 
'X':10, 
'L':50, 
'C':100, 
'D':500, 
'M':1000
}

initialMessage = "Enter the number you want translated. Limit between 1-5000:"
numberHigh = "Please enter a number between 1-5000"
noZero = "The Romans did not have the concept of Zero!"
notRoman = "This is not a roman numeral. Please enter an interger >= 5000 OR a string including only characters from the following list: I, V, X, L, C, D, and/or M"
fewer = "Please enter fewer than 17 characters"

def sanitizeInput(userInput):
	# check for int
	try: 
		userInput = int(userInput)
		ToRomanNums(userInput)

	except:
		# sanitize user input
		nums = userInput.upper()
		nums = list(nums)

		toRoman = True

		# check that the number entered is not too large; the longest roman numeral under 5000 is 16 characters long
		if len(nums) > 16: 
			print(fewer)
			# quit if number does not conform to requirements
			return

		if Roman(nums): 
			print(romanTranslator(translateList(nums)))
			return
		else: 
			print(notRoman)

			 

def ToRomanNums(num):
	if num > 5000: 
		print(numberHigh)
		return
	if num == 0: 
		print(noZero)
		return

	print('Arabic Number %s' %num)
	return


def Roman(nums): 
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
			# if (rDict[userInput[i]] % 10): 
			# 	print("V, L, and D are never used to reduce roman numerals.")
			# 	return

		else: 
			total += userInput[i]
		i+=1

	return(total)


	 


userInput = raw_input(initialMessage)
sanitizeInput(userInput)
