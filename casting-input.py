#Casting Means just we can change the data type  view the example.

a = "10"
b = "20"
print(a+b) # Now see the ouput its show like this 1020.
#why it cannot add means we decleare as the string so it contation not doing the addtion.

#By using the casting we can get the correct output 
num1 = int ("10")
num2 = int ("20")
ans = num1 + num2 
print(ans) #Now see the output it adds that two values.

a = input("Enter a:")
b = input("Enter b:")
c = a+b  # inisde this input() -  function its considered the value as a string not a numeric value. 
print(c)

# So AVoid this we mentioned the data type before we craeted the input() -function.
a = int(input("Enter a :"))
b = int(input("Enter b :"))
c = a+b
print(c)