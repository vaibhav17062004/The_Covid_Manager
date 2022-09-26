# covid_registration_system
while True:
    print("***************Welcome to covid help portal***************")
    print('''Services we provide:
        1) Vaccine slot booking
        2) Available vaccination centres
        3) Plasma donation
        4) Apply for an E-pass
        5) Vaccination stats/Covid updates
        6) Vaccination certificate
        7) Covid helpline numbers
        8) Covid guidelines to follow
        9) Buy covid related items
        10) Do a quick covid self check
        11) Exit''')
    Select_choice = int(input("Select any one from the above choices"))
    fil1 = open("eng.txt", "r")
    dil1 = fil1.read()
    import csv
    import webbrowser

    chrome = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"


    def phone_check(Phone_number):
        if len(str(Phone_number)) != 10:
            return True
        return False


    if Select_choice == 1:
        Age = int(input("Enter your age: "))
        if Age < 18:
            print("Vaccination for your age group hasn't started yet")
            break
        Phone_number = int(input("Please enter your phone number: "))
        if phone_check(Phone_number):
            print("Enter valid phone number and try again")
            continue
        name = input("Please enter your name: ")
        gender = input("Gender:- M/F/O: ")
        Aadhar_card_number = str(input("please enter your Aadhar card number: "))
        Son_daughter_of = input("S/0,D/0: ")
        State = input("Enter your state: ")
        Districts = input("Enter your district: ")
        f = open("details.csv", "a")
        d1 = csv.writer(f)
        d1.writerow([Age, Phone_number, name, gender, Aadhar_card_number, Son_daughter_of, State, Districts])
        f.close()
        f1 = open("lalli.csv", "r")
        flag = False
        d = csv.reader(f1)
        for i in d:
            if i[0] == Districts:
                if int(i[2]) > 10:
                    flag = True
        if flag == False:
            print("Vaccines not available in your district please try again ")
            continue
        elif flag == True:
            print('''Vaccines are available
            to check the centres please press 2''')
            pass  # baadme_dekhlena_please
    elif Select_choice == 2:
        Districts = input("enter your district")
        f2 = open("centre.csv", "r")
        d = csv.reader(f2)
        for i in d:
            if i[0] == Districts:
                print("Nearest vaccination centre is", i[1])
    elif Select_choice == 3:
        Age = int(input("Enter your age: "))
        if Age < 18:
            print("Sorry you cannot donate your plasma as you're underage")
            continue
        Blood_group = input("Enter your blood group")
        Phone_number = int(input("Please enter your phone number: "))
        if phone_check(Phone_number):
            print("Enter valid phone number and try again")
            continue
        name = input("Please enter your name: ")
        gender = input("Gender:- M/F/O: ")
        Districts = input("Please enter your district")
        f3 = open("centre.csv", "r")
        d = csv.reader(f3)
        for i in d:
            if i[0] == Districts:
                print("Nearest plasma donation centre", i[1], Districts)
    elif Select_choice == 4:
        Districts = input("Please enter your current location: ")
        Districts2 = input("Please enter your final destination: ")
        Covid_report_id = int(input("Please enter your covid report id: "))
        Vaccination_status = input("Are you vaccinated(Y/N)")
        Travel_purpose = input("Please specify the reason of travel: ")
        Transportation_mode = input('''Please specify the mode of transportation:
            Two wheeler
            Four wheeler
            Public transport: ''').lower()
        if Transportation_mode == "public transport":
            Choice = input('''Please specify the transportation service:
                Bus
                Cab(Four wheeler)
                Motocab
                Train
                Plane service: ''').lower()
        elif Transportation_mode == "Two wheeler":
            choice1 = str(input("Please enter your vehicle registered number: "))
        elif Transportation_mode == "Four wheeler":
            choice2 = str(input("Please enter your vehicle registered number: "))
        import random

        E_pass_generator = (random.randint(12000, 50000))
        if Vaccination_status == "Y":
            print("E-pass is available\n", "E-pass id:", E_pass_generator, "\nTravelling", "From", Districts, "to",
                  Districts2, "\n Transportation mode=", Transportation_mode)
    elif Select_choice==5:
        choice123=int(input('''Please select the preferred option
        Press 1 to view Vaccination Status
        Press 2 to view the Covid updates'''))
        if choice123==1:
            d = { "World wide   ":[ "394Cr", '109Cr ','13.9%'],
            "India        ": ['44.2Cr', "9.54Cr","7.0%"],
            "United States": ["34.2Cr","16.3Cr","49.7%"]}
            print("country      ","\t",["Doses given","Fully vaccinated","% of population fully vaccinated"])
            for i in d:
                print(i,"\t",d[i])
            choice1234=int(input('''Please select the option:
            Press 1 to view world vaccination stat graph
            Press 2 to view India's vaccination stat graph'''))
            if choice1234==1:
                import cv2
                from matplotlib import pyplot as plt
                img=cv2.imread("world.png",-1)
                cv2.imshow("image",img)
                plt.imshow(img)
                plt.show()
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            elif choice1234==2:
                import cv2
                from matplotlib import pyplot as plt
                img = cv2.imread("india.png", -1)
                cv2.imshow("image", img)
                plt.imshow(img)
                plt.show()
                cv2.waitKey(0)
                cv2.destroyAllWindows()
        if choice123==2:
            c1234=int(input('''Covid updates:
            Press 1 to see covid updates of the world
            Press 2 to see India's covid updates'''))
            if c1234==1:
                import cv2
                from matplotlib import pyplot as plt
                img = cv2.imread("casesworld.png", -1)
                cv2.imshow("image", img)
                plt.imshow(img)
                plt.show()
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            elif c1234==2:
                import cv2
                from matplotlib import pyplot as plt
                img = cv2.imread("indiacase.png", -1)
                cv2.imshow("image", img)
                plt.imshow(img)
                plt.show()
                cv2.waitKey(0)
                cv2.destroyAllWindows()
    elif Select_choice==6:
        name = input("Please enter your name: ")
        Vaccination_id = int(input("Please enter your vaccination id: "))
        ADD = input("Please enter your address: ")
        Age = int(input("Please enter your age"))
        Gender = input("Please enter your gender M/F/0: ")
        Aadhar_card_id = input("Please enter your aadhar card id")
        Email_id = input("please enter your email id: ")
        print(" Name            \t", name, "\n", "Vaccination_id  \t", Vaccination_id, "\n", "Address         \t", ADD,
              "\n", "Gender          \t", Gender, "\n", "Aadhar card     \t", Aadhar_card_id, "\n")
        import pyttsx3
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[-2].id)  # voice change
        engine.setProperty('rate', 160)# speed
        s="hello  "+  name + " " + "   Your E Vaccination certificate has been successfully sent to your registered email address    " + Email_id
        engine.say(s)
        engine.runAndWait()
    elif Select_choice == 7:
        c7 = int(input('''Please select the preferred option:
            Press 1 To get the covid helpline numbers:
            Press 2 To get the covid helpline number of your district hospital:
            Press 2 To get covid helpline email:'''))
        if c7 == 1:
            print("The covid helpline no. is:   1075")
        elif c7 == 2:
            Districts = input("Please enter your district: ")
            f = open("centre.csv", "r")
            d = csv.reader(f)
            for i in d:
                if i[0] == Districts:
                    print("Nearest vaccination centre is", i[1], "Helpline no. is", i[2])

        elif c7 == 3:
            print("gmail id:- ncov2019@gmail.com")
    elif Select_choice == 8:
        choice3 = int(input('''Select the choice to view the covid guidelines
            Press 1 to read the Covid guidelines
            Press 2 to watch video related to Covid guidelines'''))
        if choice3 == 1:
            print(dil1)
        elif choice3 == 2:
            webbrowser.get(chrome).open_new("https://youtu.be/IT7ghcGy6r0")

    elif Select_choice == 9:
        choice4 = int(input('''Select the things to buy:
            Press 1) To buy oximeter
            Press 2) To buy sanitiser
            Press 3) To buy thermometer
            Press 4) To buy PPE kit
            Press 5) To buy oxygen cylinders
            Press 6) To buy masks
            Press 7) To buy coronil kit
            Press 8) To buy medicines'''))
        if choice4 == 1:
            webbrowser.get(chrome).open_new("shorturl.at/gmuOX")
        elif choice4 == 2:
            webbrowser.get(chrome).open_new("t.ly/LfqA")
        elif choice4 == 3:
            webbrowser.get(chrome).open_new("t.ly/xO8M")
        elif choice4 == 4:
            webbrowser.get(chrome).open_new("t.ly/4rMz")
        elif choice4 == 5:
            webbrowser.get(chrome).open_new("t.ly/rh6r")
        elif choice4 == 6:
            webbrowser.get(chrome).open_new("t.ly/soqT")
        elif choice4 == 7:
            webbrowser.get(chrome).open_new("t.ly/4481")
        elif choice4 == 8:
            webbrowser.get(chrome).open_new("t.ly/pCQG")
    elif Select_choice == 10:
        print("Thank you for coming forward for your test...")
        cough = input("Are you having cough?(y/n): ").lower()
        dry_cough = "n"
        cough_1 = "n"
        if (cough == "y" or cough == "Y"):
            dry_cough = input("Are you having dry cough?(y/n): ").lower()
            cough_1 = input("Are you having normal cough?(y/n): ").lower()
        sneeze = input("Are you having cold?(y/n): ").lower()
        pain = input("Are you having pain in your body?(y/n): ").lower()
        weakness = input("Are you feeling weak?(y/n): ").lower()
        itemp = int(input("Please enter your temperature in celcius: "))
        if (itemp <= 98.6):
            temp = "low"
        else:
            temp = "high"
        breathe = input("Are you facing difficulty in breathing?(y/n): ").lower()
        if (
                dry_cough == "y" and sneeze == "y" and pain == "y" and weakness == "y" and temp == "high" and breathe == "y"):
            print('''According to the information provided by you
            you might be suffering from Corona
            It is advised to be home isolated otherwise you can consult the doctor ''')
            ccc = int(input("Press 1 to see covid prevention video else press 0"))
            if ccc == 1:
                webbrowser.get(chrome).open_new("https://youtu.be/JajhtnELhnM")
            elif ccc == 0:
                print("Thank you for visiting the covid help portal stay at home and stay safe: ")
        elif (
                dry_cough == "y" and sneeze == "y" and pain == "n" and weakness == "n" and temp == "low" and breathe == "n"):
            print('''Nothing to worry it's just common cold
            but you're advised to take rest at your home ''')
            cc = int(input(
                "Press 1 if you further want to see the protocols to be followed while in home isolation Else press 0: "))
            if cc == 1:
                webbrowser.get(chrome).open_new("https://youtu.be/ijVneNt6eOo")
            elif cc == 2:
                print("Thank you for visiting the covid help portal stay at home and stay safe: ")
        else:
            print("Do not worry you are fine: ")


    elif Select_choice == 11:
        print("Thank you for visiting the covid help portal stay at home and stay safe: ")
        break



