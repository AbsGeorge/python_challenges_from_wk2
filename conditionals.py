grade = int(input("Enter mark "))

print(grade)

if grade > 85:
    print("Distinction")

elif grade <= 85 and grade >= 65:
    print("Pass")

else:
    print("Fail")