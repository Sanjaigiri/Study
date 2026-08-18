#if-else statement 
#by using this statement if true means it goes inisde the if statement 
# otherwise it goes to the else statement.
'''
    Syntax:
    if(condtion):
        print("") // inside any anything we give like return a  function or anything 
    else:
        print("") // we cannot give only print statement .
'''

#Eg-1
meghna = input("enter somethings for meghana:")
if(meghna == "died"):
    print("Surya Meets Priya")
else:
    print("Surya Weds meghana")

#EG-2
Std_mark=int(input("Enter a Mark:"))
if(Std_mark>=35):
    print("The Student is PASS")
else:
    print("The Student is FAIL")

#EG-3
income = int(input("Enter a Income:"))
if(income>7000):
    print("Scholarship AVailable")
else:
     print("Scholarship Not AVailable")

#The number can be divisor yes /no  how to find it .
#the numbers is  divisbled & solved in '0' - means it will be divisible.
#2/10 = 0 - the 2 is the divisble by 10 its possible .

# % - this symbol give the reminder of the value "Modular."
#and,or,not -binary opeartor
#and - two condtion,or - single condtion & atleast one condtion ,not - opposite to that condtion.
num=int(input("Enter a value  for num:"))
if(num%3 ==0 and num%5 ==0):
    print("The number is divisble by both 3 & 5",num)
else:
    print("The number is not divisble by both 3 & 5",num)