print("Hi")
n = float(input("Enter your marks: "))
if n >= 80:
    print("A+")
elif n >= 70:
    print("A")
elif n >= 60:    
    print("B")
elif n >= 50:    
    print("C")
elif n >= 33:   
    print("D")
elif n < 33:   
    print("HUh! You failed!")
else:
    print("Invalid marks!")  
