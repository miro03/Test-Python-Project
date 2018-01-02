import operator
import sys
check = 0

while check == 0:
	inputData = input("Enter a minimum of 2 number and 1 operator using ff format: (num, num, oper): ")
	splitData = inputData.split(",")
	lengthData = len(splitData)
	inputList = []
	operatorList = []

	for x in range(0,lengthData):
		try:
			inputList.append(float(splitData[x]))
		except:
			operatorList.append(splitData[x])
		
	for x in range(0,len(operatorList)):
		if operatorList[x] == 'c':
			sys.exit()
	
	process = {
			'+': operator.add,
			'-': operator.sub,
			'*': operator.mul,
			'/': operator.truediv,
		}

	answer = inputList[0]
	del inputList[0]
	LengthInputList = len(inputList)
	for a in range(0,LengthInputList):
		if operatorList[a] == '+' or operatorList[a] == '-' or operatorList[a] == '*' or operatorList[a] == '/':
			try:
				answer = process[operatorList[a]](answer,inputList[a])
				check = 1
			except ZeroDivisionError:
				print ("You can't divide by zero")
		else:
			print('Error: invalid character, please input valid integer, float and valid operator \nHere are the only valid operators and values:Valid operators are: +, *, -, / \n Valid values: integers and float \n Valid format: num, num, operator \n Operator should always be 1 less then the total numbers')
			check = 0
	
print (answer)