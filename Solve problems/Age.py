# def nextDay(year,month,day):
# 	"""Only for 30 days
	
# 	Args:
# 	    year (int): clear
# 	    month (int): clear
# 	    day (int ): clear
	
# 	Returns:
# 	    three int's: the next day function
# 	"""
# 	if(day<30):
# 		day += 1
# 		print(year,month,day)
# 		return year,month,day
# 	if(day==30 and month==12):
# 		year +=1
# 		month = 1
# 		day = 1
# 		print(year,month,day)
# 		return year,month,day
# 	if(day==30 and month!=12):
# 		month += 1
# 		day = 1
# 		print(year,month,day)
# 		return year,month,day
# # All months have 30days

# nextDay(1999, 12, 30)
# nextDay(2013, 1, 30)
# nextDay(2012, 12, 30)

# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
	my_bool= True
	counter=0
	arg_y,arg_m,arg_d=year1,month1,day1
	while my_bool:
		arg_y,arg_m,arg_d = nextDay(arg_y,arg_m,arg_d)
		counter += 1
		if(arg_y==year2 and arg_m==month2 and arg_d==day2):
			my_bool=False
			print(counter)
			return counter

daysBetweenDates(1,1,1,1,1,10)

def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print ("Test with data:", args, "failed")
        else:
            print ("Test case passed!")

test()


# His code
# Credit goes to Websten from forums
#
# Program defensively:
#
# What do you do if your input is invalid? For example what should
# happen when date 1 is not before date 2?
#
# Add an assertion to the code for daysBetweenDates to give
# an assertion failure when the inputs are invalid. This should
# occur when the first date is not before the second date.
#  

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
       year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False        

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!

    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3),
                  ((2013,1,1,1999,12,31), "AssertionError")]
    
    for (args, answer) in test_cases:
        try:
            result = daysBetweenDates(*args)
            if result == answer and answer != "AssertionError":
                print ("Test case passed!")
            else:
                print ("Test with data:", args, "failed")
    
        except AssertionError:
            if answer == "AssertionError":
                print ("Nice job! Test case {0} correctly raises AssertionError!\n".format(args))
            else:
                print ("Check your work! Test case {0} should not raise AssertionError!\n".format(args)   )         
test()
