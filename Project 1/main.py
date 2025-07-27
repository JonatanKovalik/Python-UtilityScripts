#Info:
#This code Is my first app in python .
#Creator Jonatan Kovalik.
#Data 29/11/2024.
#WebSites: RGBColors(https://htmlcolorcodes.com/)
import tkinter as tk
from tkinter import PhotoImage

#global
#the Username and the Password they are a random text
Username = "A,BCDEFGH,IJKLM_NOPQ,RS,Z"
Password = "A,BCDE34FGH,IJKLM_NOPQ,RS,Z565A,BCDEFGH,IJ3KLM_NOPQ,RS,ZA,BCDEFGH,IJKLM_NOPQ,RS,ZA,B56CDEFGH,IJKLM_NOPQ,RS,Z"
trys = 0

def appmain():
    print("App started")

#function_create_signupbuttonswitchhhh
def functionclickbuttonsignup():
    win.destroy()
    create_signup_window()

#function_create_loginbuttonswitchhhh
def functionclickbuttonLogin():
    signup_window.destroy()
    functionstart()

def functioncheckpasswordandusername(UserName, Enterusername, Password, EnterPassword):
    global trys
    if Enterusername != UserName or EnterPassword != Password:
        print("Error")
        trys += 1
    elif Enterusername == UserName and EnterPassword == Password:
        print("Success")
        appmain()
    elif trys == 3:
        print() #make new win

#signup window
def create_signup_window():
    global signup_window
    signup_window = tk.Tk()
    signup_window.title("SignUp")
    signup_window.geometry("1000x600")
    signup_window.config(background="#aa8aab")

    TitleText2 = tk.Label(signup_window, text="Sign Up", background="#aa8aab", font=('Arial', 60, 'bold'))
    TitleText2.place(x=360, y=50)

    UserNameText = tk.Label(signup_window, text="User Name:", background="#aa8aab", font=('Arial', 40, 'bold'))
    UserNameText.place(x=50, y=220)

    global EnterUserName2
    EnterUserName2 = tk.Entry(signup_window, font=('Arial', 20, 'bold'))
    EnterUserName2.place(x=360, y=240)
    Username = EnterUserName2.get()
    print(Username)

    PasswordText = tk.Label(signup_window, text="Password:", background="#aa8aab", font=('Arial', 40, 'bold'))
    PasswordText.place(x=50, y=340)

    global EnterPassword2
    EnterPassword2 = tk.Entry(signup_window, font=('Arial', 20, 'bold'))
    EnterPassword2.place(x=334, y=358)
    Password = EnterPassword2.get()
    print(Password)

    ButtonSiginUp = tk.Button(signup_window, text="Login", font=('Arial', 25, 'bold'), width=10, command=functionclickbuttonLogin)
    ButtonSiginUp.place(x=50, y=480)

    ButtonEnter = tk.Button(signup_window, text="Enter", font=('Arial', 25, 'bold'), width=10, background="#aa8aab", command=functionclickbuttonLogin)
    ButtonEnter.place(x=320, y=480)

    signup_window.mainloop()

#first_function_win
def functionstart():
    global win
    win = tk.Tk()
    win.title("Login")
    win.geometry("1000x600")
    icon1 = PhotoImage(file="Images/Login.png")
    win.iconphoto(True, icon1)
    win.config(background="#8aab93")

    TitleText = tk.Label(win, text="Login", background="#8aab93", font=('Arial', 60, 'bold'))
    TitleText.place(x=360, y=50)

    UserNameText = tk.Label(win, text="User Name:", background="#8aab93", font=('Arial', 40, 'bold'))
    UserNameText.place(x=50, y=220)

    EnterUserName = tk.Entry(win, font=('Arial', 20, 'bold'))
    EnterUserName.place(x=360, y=240)

    PasswordText = tk.Label(win, text="Password:", background="#8aab93", font=('Arial', 40, 'bold'))
    PasswordText.place(x=50, y=340)

    EnterPassword = tk.Entry(win, font=('Arial', 20, 'bold'))
    EnterPassword.place(x=334, y=358)

    ButtonSiginUp = tk.Button(win, text="SignUp", font=('Arial', 25, 'bold'), width=10, command=functionclickbuttonsignup)
    ButtonSiginUp.place(x=50, y=480)
    ButtonEnter = tk.Button(win, text="Enter", font=('Arial', 25, 'bold'), width=10, background="#aa8aab",
                            command=lambda: functioncheckpasswordandusername(Username, EnterUserName.get(), Password, EnterPassword.get()))
    ButtonEnter.place(x=320, y=480)

    win.mainloop()

functionstart()
