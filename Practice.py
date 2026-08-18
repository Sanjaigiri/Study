#EG-1
name = input()
age = int(input())
print("Enter a name:",name)
print("Enter a age:",age)


#EG-2

name = input()
age = int(input())
address = input()
print("Enter a name:",name)
print("Enter a age:",age)
print("Enter a address:",address)


#EG-3

a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))

mul = a*b*c

add = a+b+c

ans = mul/add

print("The Final Answer :",ans)

#EG-4
name = input("Enter a name:")
score = int(input("Enter a score:"))
deparment = input("Enter a deparment:")

print("My name is :",name)
print("My score is:",score,"/10")
print("My deparnment is:",deparment)


#EG-5
Name =input("Enter a name of a student :")
Age =int(input("Enter a age of a age:"))
Gender =input("Enter a Gender of a student:")
Tamil =float(input("Enter a Tamil Mark:"))
English =float(input("Enter a English Mark:"))
Maths =float(input("Enter a Maths Mark:"))
Science =float(input("Enter a Science Mark:"))
Computer =float(input("Enter a Computer Mark:"))
total = int(Tamil+English+Maths+Science+Computer)
average = float(total/5)
print( "=====================================================")
print("               STUDENT MARK SHEET")
print( "=====================================================")
print()
print()
print("Name     :",Name)
print("Age      :",Age)
print("Gender   :",Gender)
print()
print()
print("Tamil    :",Tamil)
print("English  :",English)
print("Maths    :",Maths)
print("Science  :",Science)
print("Social   :",Computer)
print()
print()
print("-------------------------------------------------------")
print("Total    :",total)
print("AVerage  :",average)
print("========================================================")