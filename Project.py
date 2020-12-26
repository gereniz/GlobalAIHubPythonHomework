name = input("Adınız : ")
surname = input("Soyadınız : ")
print("Kayıt Tamamlandı")

def message():
    message = print("You failed in class")
    return message

for i in range(3):
    nameResult = input("Adınızı Giriniz : ")
    surnameResult = input("Soyadınızı Giriniz :")   
    if i == 2 :
        print("Please try again later")
    if nameResult == name and surnameResult == surname: 
        print("Welcome " + nameResult + surnameResult)
        courses = ["Python","Java","C","Swift","C#","JavaScript","HTML"]
        userCourses= []
        print("En az 3 en fazla 5 kurs seçebilirsiniz")
        print("Kurs seçimini bitirmek için 9 yazınız.")
        for i in range(7):
            print("{} için {} basınız.".format(courses[i],i+1))
        try:
            for i in range(7):
                number = int(input("Kursun numarasını giriniz : "))
                if number == 9:
                    break
                else:
                    userCourses.append(courses[number])
        except:
            print("Olmayan değer girildi")
            userCourses = []
            print("Kursların : {}".format(userCourses))
            break
        if len(userCourses) < 3:
            print(message()) 
            break
        else :  
            for i in range(len(userCourses)):
                print("Kursların : {} - {} ".format(userCourses[i],i+1))
            number1= int(input("Girmek istediğin sınavın numarasını yazınız : "))
            midterm = int(input("Midterm notunuzu giriniz : "))
            final = int(input("Final notunuzu giriniz : "))
            project = int(input("Project notunuzu giriniz : "))
            exams = {"midterm":midterm,"final":final,"project":project}
            grade = (midterm*0.3)+(final*0.5)+(project*0.2)
            if grade >= 90:
                print("{} dersinden AA ile geçtiniz".format(userCourses[number1-1]))
                break
            elif 70 <= grade < 90:
                print("{} dersinden BB ile geçtiniz".format(userCourses[number1-1]))
                break
            elif 50 <= grade < 70:
                print("{} dersinden CC ile geçtiniz".format(userCourses[number1-1]))
                break
            elif 30 <= grade < 50:
                print("{} dersinden DD ile geçtiniz".format(userCourses[number1-1]))
                break
            else:
                print("{} dersinden başarısız oldunuz".format(userCourses[number1-1]))
                break
            


        
        
        
