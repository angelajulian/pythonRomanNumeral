
rDict = {
'I':1, 
'V':5, 
'X':10, 
'L':50, 
'C':100, 
'D':500, 
'M':1000
}

# look into why dictionary didn't work- pain to have duplicated list item 
rlist = ['M', 'IM', 'XM', 'CM', 'D', 'ID', 'XD', 'CD', 'C', 'IC', 'XC', 'L', 'IL', 'XL', 'X', 'IX', 'V', 'IV', 'I']
numlist = [1000, 999, 990, 900, 500, 499, 490, 400, 100, 99, 90, 50, 49, 40, 10, 9, 5, 4, 1]

# make exposed user strings easier to find/edit
initialMessage = "Enter the number you want translated. Limit between 1-4999:"
numberHigh = "Please enter a number between 1-4999"
noZero = "The Romans did not have the concept of Zero, or less than Zero!"
notRoman = "This is not a roman numeral. Please enter an interger >=4999 OR a string from the following list: I, V, X, L, C, D, and/or M"
fewer = "Please enter fewer than 21 characters"


# Functions which get and sanitize input
def sanitizeInput(userInput):
	try: 
		userInput = int(userInput)
		if (userInput<=0):
			print(noZero) 
			return
		if (userInput>4999): 
			print(numberHigh)
		ToRomanNums(userInput)
	except Exception as e: 
		confirmRoman(userInput)


def confirmRoman(userInput):
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

def ToRomanNums(userInput):
	i = 0
	outputString = ''
	# for each num in numlist
	while i < len(numlist):
		# try to divide userInput by num
		mult = userInput/numlist[i]
		# if user input is divisible by num
		if mult: 
			userInput -= (mult * numlist[i])
			# add the roman numeral times however many times num goes into user input
			outputString = outputString + (rlist[i]*mult)
		i += 1
	print(outputString)


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
	# takes a list of chars from rDict
	# replaces all items in list with ints from rDict
	for i, item in enumerate(userList):
		userList[i] = rDict[item]
	return userList


def romanTranslator(userInput): 
	# takes a list of ints
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
