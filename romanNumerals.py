


rDict = {
'I':1, 
'V':5, 
'X':10, 
'L':50, 
'C':100, 
'D':500, 
'M':1000
}


def sanitizeInput(userInput):
	# sanitize user input
	nums = userInput.upper()
	nums = list(nums)

	fromRoman = True
	toRoman = True

	# check that the number entered is not too large; the longest roman numeral under 5000 is 16 characters long
	if len(nums) > 16: 
		print("Please enter a number between 1-5000")
		# quit if number does not conform to requirements
		return

	# check if all char are roman numerals
	for num in nums:
		if num in rDict: 
			fromRoman *= True
		else:
			fromRoman *= False
			#if not roman numeral, check if INT
			try: 
				int(nums)
			except: 
				print("Please enter roman numberals (I,V,X,L,C,D or M) or an integer.")

	if fromRoman == True:
		romanTranslator(nums) 


def romanTranslator(userInput): 
	# if the input passes sanitation only
	total = 0
	length = len(userInput)
	i = 0 

	while i < length: 
		if i == (length - 1): 
			total += rDict[userInput[i]]
		# roman numerals only have 1 charcter less: ex 8 is VIII rather than IIX
		# TODO: This is the bullshit right here
		elif userInput[i] < userInput[(i+1)]:
			print(i)
			print("user input i is %s" % rDict[userInput[i]])
			print("user input i+1 is %s" % rDict[userInput[i+1]])
			print( rDict[userInput[i]] >  rDict[userInput[i+1]])
			total -= rDict[userInput[i]]
			# if (rDict[userInput[i]] % 10): 
			# 	print("V, L, and D are never used to reduce roman numerals.")
			# 	return

		else: 
			total += rDict[userInput[i]]
			print(i)
			print("user input i is %s" % rDict[userInput[i]])
			print("user input i+1 is %s" % rDict[userInput[i+1]])
			print( rDict[userInput[i]] >  rDict[userInput[i+1]])
		i+=1

	print(total)


	 


userInput = raw_input("Enter the number you want translated. Limit between 1-5000:")
sanitizeInput(userInput)
