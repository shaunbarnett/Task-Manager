# Task-Manager

In this task, I created a program for a small business that can
help it to manage tasks assigned to each member of the team. This program will work with two text files, user.txt and tasks.txt.

tasks.txt stores a list of all the tasks that the team is working on. The data for each task is stored on a separate line in the text file. Each line includes
the following data about a task in this order:

■ The username of the person to whom the task is assigned.
■ The title of the task.
■ A description of the task.
■ The date that the task was assigned to the user.
■ The due date for the task.
■ Either a ‘Yes’ or ‘No’ value that specifies if the task has been
completed yet.

user.txt stores the username and password for each user that has permission to use the program (task_manager.py). The username and password for each
user must be written to this file in the following format:

■ First, the username followed by a comma, a space and then the password.
■ One username and corresponding password per line.

My program allows users to do the following: 
Login. The user will be prompted to enter a username and password. A list of valid usernames and passwords are stored in a text file called user.txt. An error message is displayed if the user enters a username that is not listed in user.txt or enters a valid username but not a valid password. The user should repeatedly be asked to enter a valid username and password until they provide
appropriate credentials.

The following menu should be displayed once the user has successfully logged in:

Please select one of the following options:
r - register user
a - add task
va - view all tasks
vm - view my tasks
e - exit

If the user chooses ‘r’ to register a user, the user will be prompted for a new username and password. The user will also be asked to confirm the password. If the value entered to confirm the password matches the value of the password, the username and password should be written to user.txt in the appropriate format.

If the user chooses ‘a’ to add a task, the user will be prompted to enter the username of the person the task is assigned to, the title of the task, a description of the task and the due date of the task. The data about the new task will be written to tasks.txt. The date on which the task is assigned should be the current date. Also, whenever a user adds a new task, the value that indicates whether the task has been completed or not is ‘No’.

If the user chooses ‘va’ to view all tasks, The information for each task will be displayed on screen in an easy to read format.

If the user chooses ‘vm’ to view the tasks that are assigned to them,
tasks that have been assigned to the user that is currently logged-in is displayed on screen in a user-friendly, easy to read manner.

Only the user with the username ‘admin’ is allowed to register users. The admin user is provided with a new menu option that allows them to display statistics. When this menu option is selected, the total number of tasks and the total number of users will be displayed in a user-friendly manner..





