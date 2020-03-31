def calculator():

	#input parameters

	no1=float(input("Enter first number: "))

	no2= float(input("Enter Second number: "))

	op= input ("Enter operator symbol: ")

	#operations
	
	if op == '+':

		add=no1+no2;
		print(str(no1)+" + "+str(no2)+" = "+str(add))

		answer=input("Do you wish to perform  another operation?(Y/N) ")
		
		if answer == 'Y' or answer=='y':
			calculator()
		
		else:
			exit()
	
	elif op == '-':

		substraction=no1-no2
		print(str(no1)+" - "+str(no2)+" = "+str(substraction))
		
		answer=input("Do you wish to perform another operation?(Y/N) ")
		
		if answer == 'Y' or answer=='y':
			calculator()
		
		else:
			exit()
	
	elif op == '*':

		multiplication=no1*no2;
		print(str(no1)+" * "+str(no2)+" = "+str(multiplication))
		
		answer=input("Do you wish to perform another operation?(Y/N) ")
		
		if answer == 'Y' or answer=='y':
			calculator()
		
		else:
			exit()
	
	elif op == '/':
		if no2 == 0:
			print("Operation cannot be performed.")
	
		else:
			division=no1/no2;
			print(str(no1)+" / "+str(no2)+" = "+str(division))
			
			answer=input("Do you wish to perform another operation?(Y/N) ")
		
			if answer == 'Y' or answer=='y':
				calculator()
		
			else:
				exit()

	elif op == '%':
		if no2 == 0:
			print("Operation cannot be performed.")
	
		else:
			modulus=no1%no2;
			print(str(no1)+" % "+str(no2)+" = "+str(modulus))
			
			answer=input("Do you wish to perform another operation?(Y/N) ")
		
			if answer == 'Y' or answer=='y':
				calculator()
		
			else:
				exit()
		
	else:

		print("You have entered an invalid operator")
		
		
#function call

calculator()