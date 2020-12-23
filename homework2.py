firstName = input("First Name : ")
lastName = input("Last Name : ")
age = int(input("Age : "))
dateOfBirth = int(input("Date of Birth : "))

liste=[]
liste.append(firstName)
liste.append(lastName)
liste.append(age)
liste.append(dateOfBirth)
for value in liste:
    print("{}".format(value))
if age < 18:
    print("You can't go out because it's too dangerous")
else :
    print("You can go out on the street")
