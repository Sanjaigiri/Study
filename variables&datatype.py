# A variable is the container to stores a values .
'''  The varaibles types are :
    Category	Data Types	    Example
    1.Numeric	int	            10
	            float	        10.5
	            complex	        10 + 5j
    2.Sequence	str	            "Hello"
	            list	        [1, 2, 3]
	            tuple	        (1, 2, 3)
	            range	        range(5)
    3.Mapping	dict	        {"name": "Sanjai", 
                                 "age": 23
                                }
    4.Set	    set	            {1, 2, 3}
	            frozenset	    frozenset({1, 2, 3})
    5.Boolean	bool	        True, False
    6.Binary	bytes	        b"Hello"
	            bytearray	    bytearray(5)
	            memoryview	    memoryview(bytes(5))
    7.None	    NoneType	    None
'''
#Numeric - int,float,complex

#EG-1:

a = 10
b = 20
c = a+b 
print("The answer is:",c)


#EG-2:

a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = a+b

print("The value of adding a & b is :",c)


#Eg-3

std_name = input("Enter a Name:")
std_score = float(input("Enter a Score:"))
std_gender = input("Enter a gender:")

result = [
{
    "Staff_name": "Sanjai",
    "Staff_age":  20,
    "Staff_college": "KPR College",
},
{
    "staff_name": "Mohan",
    "Staff_age":  22,
    "Staff_college": "KPR College" 

       
}
]
print("The III - Bsc (CS) Data's")
print("The Students Detials")
print("The Student name is:",std_name)
print("The Student score is:",std_score/10,"/10")
print("The Student gender is:",std_gender)
print("The Staff Details")
print(result)

#Rest of Data Type we can see later