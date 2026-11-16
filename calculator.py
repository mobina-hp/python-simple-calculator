first_number = float(input("enter first number :"))
operator = input("enter operator :")
second_number = float(input("enter second number :"))

if operator == "+" : 
    result = first_number + second_number
    print(result)
    
elif operator == "-" : 
    result = first_number - second_number
    print(result)
    
elif  operator == "*" : 
    result = first_number * second_number
    print(result)
    
elif operator == "/" :
    if second_number != 0 :
        result = first_number / second_number 
        print(result)
    else :
        print("second number can not be 0")
        
else :
    print("invalid operator!")