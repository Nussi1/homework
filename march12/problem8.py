eligible = int(input('how old are you: '))
passport = int(input('do you have a passport?choose 1 - Yes, 0 - No: '))
money = int(input('How much money are you planning to spend?'))
if eligible > 18 and passport == 1 and money >= 5000:
	print('you are eligible to go to trip with us')
else: 
	print('try to submit next time')
