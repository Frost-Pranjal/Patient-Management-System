from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image, ImageEnhance
from tkinter import messagebox


def insertHospPage(win, frame, u):
    import hospitalPage.hospitalHomepage as hp
    hp.mainPage(win, frame, u)
def mainLog(win, frame):
  
    frame.destroy()

    img = Image.open("hospitalPage\images\hospital.jpg")
    resized_image = img.resize((win.winfo_width(), win.winfo_height()))

    if img.mode != "RGBA":
        img = resized_image.convert("RGBA")
    else:
        img = resized_image.copy()
    alpha = img.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(0.5)
    img.putalpha(alpha)
  
    bg = ImageTk.PhotoImage(img)
    background = Label(win, image=bg)
    background.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
    background.image = bg

    

    color ="#065a78"

    win.wm_title("Hospital Account")

    

    def login():
        u = database.getHosAuth()
        usr = usernameEntry.get()
        pas = passwordEntry.get()

        for users in u:
            if usr == users:
                if pas == database.getHpass(usr):
                    insertHospPage(win, frame, usr)
                else:
                    messagebox.showerror('Error', 'Incorrect Password')
            break
        else:
            messagebox.showerror('Error', 'This Username Doesnt Exist')



    
    
    LogFrame = LabelFrame(win, bg=color,  bd=15, relief=RIDGE)
    LogFrame.place(relx=0.5, rely=0.5, anchor=CENTER)


    usernameLabel = Label(LogFrame, text="Username:", font=('Arial',15,'normal') , pady=5, bg=color)
    usernameLabel.grid(row=0, column=0)

    usernameEntry = Entry(LogFrame, bg=color)
    usernameEntry.grid(row=0, column=1)

    passwordLabel = Label(LogFrame, text="Password:", font=('Arial',15,'normal') , pady=5, bg=color)
    passwordLabel.grid(row=1, column=0)

    passwordEntry = Entry(LogFrame, show="*", bg=color)
    passwordEntry.grid(row=1, column=1)

    import database

    logButton = Button(LogFrame, text="LOG IN", font=('Arial',12,'normal'), command=login)
    logButton.grid(row=2, column=0, columnspan=2)

    lineLabel = Label(LogFrame, text='---------------------------------------------', bg=color)
    lineLabel.grid(row=3, column=0, columnspan=2)

    signUpInfo = Label(LogFrame, text="Dont Have an Account? \n Contact Administrator at wellness.storage.project@gmail.com", font=('Arial',12,'italic'),  fg='#333333', bg=color)
    signUpInfo.grid(row=4, column=0, columnspan=2)
