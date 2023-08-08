import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import csv
import re

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")
        
        # Background_image
        self.bg = ImageTk.PhotoImage(file="images/background.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        
        # Login Frame
        Frame_login = Frame(self.root, bg="#A7DAEA")
        Frame_login.place(relx=0.5, rely=0.5, width=500, height=400, anchor=tk.CENTER)

        # Title
        title = Label(Frame_login, text="Hello There!", font=("Terminal", 30, "bold"), fg="black", bg="#A7DAEA")
        title.pack(anchor=tk.N)
        
        # Subtitle
        subtitle = Label(Frame_login, text="You are not logged in to our system", font=("Terminal", 10, "bold"), fg="black", bg="#A7DAEA")
        subtitle.pack(anchor=tk.N)
        
        # Username
        label_user = Label(Frame_login, text="Username", font=("Terminal", 15, "bold"), fg="black", bg="#A7DAEA")
        label_user.pack(anchor=tk.NW)
        self.username_entry = Entry(Frame_login, font=("System", 15), bg="#A7DAEA")
        self.username_entry.pack(anchor=tk.NW)
        
        # Password
        label_password = Label(Frame_login, text="Password", font=("Terminal", 15, "bold"), fg="black", bg="#A7DAEA")
        label_password.pack(anchor=tk.NW)
        self.password_entry = Entry(Frame_login, show="*", font=("System", 15), bg="#A7DAEA")
        self.password_entry.pack(anchor=tk.NW)
        
        # Button - forgot password?
        forgot_button = Button(Frame_login, text="Forgot password?", bd=0, font=("Terminal", 7, "bold"), fg="black", bg="#A7DAEA")
        forgot_button.pack(anchor=tk.NW)
        
        # Button - Login
        login_button = Button(Frame_login, command=self.login_user, text="Login", font=("Terminal", 7, "bold"), fg="black", bg="#A7DAEA")
        login_button.pack(anchor=tk.NW, side="left")
        
        # Button - Register
        register_button = Button(Frame_login, command=self.register, text="Register", font=("Terminal", 7, "bold"), fg="black", bg="#A7DAEA")
        register_button.pack(anchor=tk.NW, side="left")
    
    def user_password_consistency(self, username, password):
        try:
            with open('user_credentials.csv', 'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if len(row) >= 2 and username == row[0] and password == row[1]:
                        return True
            return False
        except Exception as e:
            print("Error while reading CSV:", e)
            return False

    def password_validation(self, password):
        # Check if the password meets the criteria
        # Minimum 10 characters, 1 capital letter, 1 special character, and 1 digit
        if len(password) < 10:
            return False

        if not any(char.isdigit() for char in password):
            return False

        if not any(char.isupper() for char in password):
            return False

        if not any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?\'\"' for char in password):
            return False
        return True
    
    def register(self):
        # Create a new registration window
        registration_window = tk.Toplevel(self.root, bg="#94F433")
        registration_window.title("Register")
        
        # Create and arrange widgets for registration
        username_label = Label(registration_window, text="Username:", font=("Terminal", 15, "bold"), fg="black", bg="#94F433")
        username_label.pack(anchor=tk.CENTER)
        username_entry = Entry(registration_window)
        username_entry.pack()

        password_label = Label(registration_window, text="Password:", font=("Terminal", 15, "bold"), fg="black", bg="#94F433")
        password_label.pack(anchor=tk.CENTER)
        password_entry = Entry(registration_window, show="*")
        password_entry.pack()
        
        password_spec_label = Label(registration_window, text="Password must have at least 10 characters, 1 capital letter, 1 special character, and 1 digit.", 
                                    font=("Terminal", 10, "bold"), fg="red", bg="#94F433")
        password_spec_label.pack()
        
        confirm_password_label = Label(registration_window, text="Confirm Password:", font=("Terminal", 15, "bold"), fg="black", bg="#94F433")
        confirm_password_label.pack(anchor=tk.CENTER)
        confirm_password_entry = Entry(registration_window, show="*")
        confirm_password_entry.pack()

        def check_username_exists(username):
            # Check if the username exists in the CSV file
            with open('user_credentials.csv', 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if len(row) >= 1 and username == row[0]:
                        return True
            return False

        def register_new_user():
            # Add your registration logic here
            username = username_entry.get()
            password = password_entry.get()
            confirm_password = confirm_password_entry.get()
    
            if password == confirm_password:
                if check_username_exists(username):
                    messagebox.showerror("Error", "Username already exists. Please choose a different username.")
                elif self.password_validation(password):
                    # Registration successful, close the registration window
                    registration_window.destroy()
                    messagebox.showinfo("Success", "Registration successful!")
    
                    # Store username and password in the CSV file
                    with open('user_credentials.csv', 'a', newline='') as csvfile:
                        fieldnames = ['Username', 'Password']
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
                        # Check if the file is empty to write the header
                        csvfile.seek(0, 2)  # Go to the end of file
                        if csvfile.tell() == 0:
                            writer.writeheader()
    
                        writer.writerow({'Username': username, 'Password': password})
                else:
                    messagebox.showerror("Error", "Password must have at least 10 characters, 1 capital letter, 1 special character, and 1 digit!")
            else:
                messagebox.showerror("Error", "Passwords do not match!")

        register_button = Button(registration_window, text="Register", command=register_new_user)
        register_button.pack()

    def login_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.user_password_consistency(username, password):
            messagebox.showinfo("Login successful!", "Welcome, " + username)
            self.root.destroy()  # Close the login window
            self.show_welcome_window()
        else:
            messagebox.showerror("Login failed.", "Invalid credentials.")

    def show_welcome_window(self):
        # Create a new instance of Tk for the WelcomeWindow
        welcome_window = tk.Tk()
        welcome_obj = WelcomeWindow(welcome_window)
        welcome_window.mainloop()

class WelcomeWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome!")
        self.root.geometry("400x300")  # Set the size of the window

        # Background_image (If needed, replace 'background.jpg' with the actual background image path)
        self.bg = ImageTk.PhotoImage(file="images/background.jpg")
        self.bg_label = Label(self.root, image=self.bg)
        self.bg_label.pack(fill=BOTH, expand=YES)

if __name__ == "__main__":
    root = Tk()
    obj = Login(root)
    root.mainloop()
