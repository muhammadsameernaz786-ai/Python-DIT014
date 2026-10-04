age = int(input("enter your age in numbers = "))
student_check = input("are you a student ? (yes or no) : ").lower()

if age < 0 or age > 120 :
    category = "Invalid Age"
    print(category)
elif age < 18 :
    category = "Child"
    price = 15
    print(f"Category : {category} and Price : {price}sek")
elif 18<= age <= 25 and student_check == "yes" :
    category = "student"
    price = 24
    print(f"Category : {category} and Price : {price}sek")
elif age >= 65 :
    category = "Senior"
    price = 20
    print(f"Category : {category} and Price : {price}sek")  
else :
    category = "Adult"
    price = 36
    print(f"Category : {category} and Price : {price}sek")

    
    