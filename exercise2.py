#num1=input("Enter 1st num")
#num2=input("Enter 2nd num")
#num3=input("Enter 3rd num")
#1st step without comma
num1,num2,num3=input("Enter three numbers comma seprated").split(",")#2n step with comma
print(f"avrage of three numbers : {int(num1) + int(num2) + int(num3)/3}")
