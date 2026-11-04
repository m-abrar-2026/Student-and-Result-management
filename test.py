student={}
while True:
    print('\n---------Student Manager---------')
    print("1.Add Student")
    print("2.View Student")
    print("3.Check Result")
    print("4.Delete Student")
    print("5.update")
    print("6.Exit")


    choice=input("Enter your choice: ")

    if choice=="1":
        name=input("Enter your name: ")
        Marks=int(input("Enter your Marks: "))
        student[name]=Marks
        print(f"{name} Successfully added!")

    elif choice=="2":
        if not student:
            print("No student found!!!")
        else:
            for name,Marks in student.items():
                print(name,":",Marks)


    elif choice=="3":
        name=input("Enter your name: ")

        if name in student:
            Marks = student[name]

            if Marks>=35:
                print(f"{name}: Pass")
            else:
                print(f'{name}: 1Failed')
        else:
            print(f"{name} does not exist")

    elif choice=="4":
        name = input("Enter your name: ")
        if name in student:
            student.pop(name)

            print(f"{name} Successfully removed")


    elif choice=="5":
        name = input("Enter your name: ")
        Marks = int(input("Enter your Marks: "))
        student.update({name:Marks})

        print(f"{name} Successfully updated ")


    elif choice=="6":
        print("Exiting...")
        break


    else:
        print("Invalid input please enter any choice from above")
















