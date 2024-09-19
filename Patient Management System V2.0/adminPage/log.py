from tkinter import *
from PIL import ImageTk, Image, ImageEnhance
from tkinter import messagebox

def insertAdminPage(win, frame, usrN):
    import adminPage.adminHomepage as adhp
    adhp.mainPage(win, frame, usrN)

def mainLog(win, frame):
    frame.destroy()
    color ="#8e9db2"   

    win.wm_title("Admin Account")

    img = Image.open("adminPage/images/adminWallpaper.jpg")
    resized_image = img.resize((win.winfo_width(), win.winfo_height()))

    if img.mode != "RGBA":
        img = resized_image.convert("RGBA")
    else:
        img = resized_image.copy()
    alpha = img.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(0.65)
    img.putalpha(alpha)
  
    bg = ImageTk.PhotoImage(img)
    background = Label(win, image=bg)
    background.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
    background.image = bg

    def login():
        u = database.adminAuth()
        usr = usernameEntry.get()
        pas = passwordEntry.get()

        for users in u:
            if usr == users:
                if pas == database.adminPass(usr):
                    insertAdminPage(win, frame, usr)
                else:
                    messagebox.showerror('Error', 'Incorrect Password')
            break
        else:
            messagebox.showerror('Error', 'This Username Doesnt Exist')

    LogFrame = LabelFrame(win, bg=color, bd=15, relief=RIDGE)
    LogFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

    usernameLabel = Label(LogFrame, text="Username:", font=('Arial',15,'normal') , bg=color, pady=5)
    usernameLabel.grid(row=0, column=0)

    usernameEntry = Entry(LogFrame)
    usernameEntry.grid(row=0, column=1, padx=20)

    passwordLabel = Label(LogFrame, text="Password:", font=('Arial',15,'normal') , bg=color, pady=5)
    passwordLabel.grid(row=1, column=0)

    passwordEntry = Entry(LogFrame, show="*")
    passwordEntry.grid(row=1, column=1, padx=20)

    import database

    logButton = Button(LogFrame, text="LOG IN", font=('Arial',12,'normal'), command=login)
    logButton.grid(row=2, column=0, columnspan=2)