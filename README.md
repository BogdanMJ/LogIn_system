# LogIn_system
The program represents a simple login system using a graphical window with the `tkinter` module. Users can register new accounts and log in using existing credentials. After successful login, the program displays a welcome window.

Description of Each Function:
 
1.       `user_password_consistency(self, username, password)`
a.       This function checks the consistency of the given username and password with the data in the CSV file `user_credentials.csv`,             which stores registered users' information.
b.       It returns `True` if the combination of username and password is found in the file; otherwise, it returns `False`.
 
2.       `password_validation(self, password)`
a.       This function validates if the given password meets the required criteria:
b.       At least 10 characters,
c.       At least 1 uppercase letter,
d.       At least 1 special character,
e.       At least 1 digit.
f.        It returns `True` if the password meets the requirements; otherwise, it returns `False`.
 
3.       `register(self)`
a.       This function creates a new registration window (`registration_window`) where users can enter their registration data.
b.       It checks if the entered username already exists in the CSV file.
c.       If the password matches the confirmation and meets the criteria, it saves the user's data to the CSV file.
 
4.       `check_username_exists(username)`
a.       This helper function checks if the given username already exists in the CSV file.
b.       It returns `True` if the username exists; otherwise, it returns `False`.
 
5.       `register_new_user()`
a.       This function is called when registering a new user.
b.       It retrieves the data entered by the user in the registration window.
c.       It checks if the password meets the criteria and if the confirmation password matches.
d.       It displays appropriate messages in case of errors or successful registration.
 
 
6.       `login_user(self)`
a.       This function is called when attempting to log in.
b.       It retrieves the data entered by the user in the login window.
c.       It checks the given data against the data in the CSV file.
d.       It displays appropriate messages for successful or unsuccessful login attempts.
 
7.       `show_welcome_window(self)`
a.       This function is called after a successful login.
b.       It creates a new welcome window (`welcome_window`) with a welcome message to the user.
 
8.       `WelcomeWindow`
a.       This class represents the welcome window (created after successful login).
 
9.       `__init__(self, root)`
a.       The constructor of the `WelcomeWindow` class.
b.       It initializes the welcome window (`root`) and sets its title and size.
 
Explanation of Each Function's Logic:
 
1.       `__init__(self, root)`
a.       Initializes the main login window (`root`) and sets its title and size.
b.       Creates a background image for the login window based on the `background.jpg` image file.
c.       Contains comments describing each step of the login window configuration.
 
2.       `register(self)`
a.       Creates a new registration window (`registration_window`) with a background image based on `background.jpg`.
b.       Adds interactive widgets (labels, entry fields, buttons) to the registration window.
c.       Calls functions responsible for checking if the username already exists and for saving new user data.
d.       Contains comments explaining the registration process.
 
3.       `check_username_exists(username)`
a.       Opens the `user_credentials.csv` file and checks if the given username exists.
b.       Returns `True` if the username exists; otherwise, returns `False`.
c.       Contains a comment explaining the purpose of this function.
 
4.       `register_new_user()`
a.       Retrieves data entered by the user (username, password, and password confirmation).
b.       Checks if the password meets the criteria (at least 10 characters, 1 uppercase letter, 1 special character, and 1 digit).
c.       Checks if the given username already exists in the CSV file.
d.       If the data is valid and the username is not taken, adds the new user to the CSV file and displays a message about successful             registration.
e.       Contains comments explaining the steps of the registration process and how password validation works.
 
5.       `login_user(self)`
a.       Retrieves data entered by the user (username and password).
b.       Checks the given data against the data in the CSV file.
c.       Displays appropriate messages for successful or unsuccessful login attempts.
d.       Contains comments explaining the functionality of the login function.
 
6.       `show_welcome_window(self)`
a.       Creates a new welcome window (`welcome_window`) with the specified size and background based on `background.jpg`.
b.       Contains a comment explaining the purpose of this function.
