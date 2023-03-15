# At this stage i am opening the file that i would like the program to read from to validate username and password.

file = open("user.txt", "r")
lines = file.readlines()

# The following lines of code checks the user input and coverts to lowercase. if user inputs their correct username and
# password, they are though to the menu stage else they will be asked repeatedly for username and password until it is correct.

while True:
    user = input("\nPlease enter username: ").lower()
    pwd = input("\nPlease enter your password: ").lower()
    for line in lines:
        words = line.strip()
        words = words.split(", ")

        if words[0] == user:
            print("\nWelcome,", user)
            break

    else:
        print("\nYou have entered an incorrect username!")

    if words[1] == pwd:
        print("\nThank you, you are now authorised")
        break

    else:
        print("Incorrect password!")

# presenting the menu to the user and making sure that the user input is converted to lower case.

while True:

    menu = input('''\nSelect one of the following Options below:     
r - Registering a user (Admins only)                                            
a - Adding a task                                                  
va - View all tasks                                                
vm - view my task 
d - Display statistics (Admins only)                                                 
e - Exit                                                           
: ''').lower()

# for option r, only admin can register a new user otherwise this service will be denied. username is entered then
# password is entered twice for confirmation and the two password entries must match! If so, a file will be opened to
# write to entries are username, comma. then a space followed by password. all inputs are converted to lowercase

    if menu == 'r':
        pass
        if user == "admin":
            user = input("Please enter  username: ").lower()
            pwd = input("Please enter password: ").lower()
            confirm = input("Please re-enter password: ").lower()
            if pwd == confirm:
                file = open("user.txt", "a")
                file.write(f"\n{user}, {pwd}")
                file.close()
                print()
                print(user, "has been registered")
            else:
                print("Passwords do not match!")

        else:
            print("\nPermissions denied!")

# option a is where users can assign tasks for other users. The tasks are in the following order that it is written in
# task.txt file: username, title, description, due date and current date. User must be a current user in the user.txt
# file. User input is converted to lowercase

    elif menu == 'a':
        pass
        user_file = open("user.txt", "r")
        user_file2 = user_file.readlines()
        user_file.close()

        user = input("\nPlease enter the username of the person whom the task is assigned to: ").lower()
        title = input("Please enter a title for this task: ").lower()
        description = input("Please give a short description: ").lower()
        date = input("Please give the due date for this task: ").lower()
        current_date = input("Please enter thr current date: ").lower()

        for u in user_file2:
            if user == u:
                file = open("tasks.txt", "a")
                file.write(f"\n{user}, {title}, {description}, {date}, {current_date}, No")
                file.close()
            print(f"\nYou have added the {title} task to {user}")
        else:
            print("Try again")




# Option va the user is displayed a user friendly view of all tasks for every user

    elif menu == 'va':
        pass
        print(f"\nHello, {user} the tasks are in the following format:")
        print("Username,  Task,  description,  Date the task commences,  Today's date,  Task completed Y/N\n")
        read = open("tasks.txt", "r")
        file = read.readlines()
        for lines in file:
            lines = lines.strip(", ")
            lines = lines.replace(", ", ",  ")
            print(lines)

# Option vw displays to user all tasks assigned to them, only.

    elif menu == 'vm':
        pass
        print(f"\nHello, {user}. Your tasks are in the following format:")
        print("Username,  Task,  description,  Date the task commences,  Today's date,  Task completed Y/N\n")
        read = open("tasks.txt", "r")
        file = read.readlines()

        for lines in file:
            lines = lines.strip(", ")
            lines = lines.replace(", ", ",  ")

            if user in lines:
                print(lines)

# Option d performs uses for loop with counters to determine the total number of users and the total of tasks looping
# through the user.txt and task.txt files respectively. Only admins can access this option.

    elif menu == 'd':
        pass
        if user == "admin":
            count = 0
            file = open("user.txt", "r")
            lines = file.readlines()
            file.close()
            for line in lines:
                count += 1
            print(f"\nTotal number of users:\t{count}")

            counter = 0
            read = open("tasks.txt", "r")
            file = read.readlines()
            for line in file:
                counter += 1
            print(f"Total number of tasks:\t{counter} ")
        else:
            print("\nPermission denied!")


# e is for exit

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
