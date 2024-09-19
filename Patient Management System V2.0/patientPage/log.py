from tkinter import *
from tkcalendar import DateEntry
from datetime import date
from tkinter import ttk
from PIL import ImageTk, Image, ImageEnhance
from tkinter import messagebox

today = date.today()

_font = ("Comic Sans MS", 19, "bold")
color ="#d3d4c4"

def enterPatientPage(win, frame, u):
    import patientPage.patientHomepage as ph
    ph.mainPage(win, frame, u)


def login(win, frame):
    for child in frame.winfo_children():
        child.destroy()

    win.wm_title("Log In")

    usernameLabel = Label(frame, text='Enter Username', width=20, bg=color, font =("Comic Sans MS", 12, "bold"))
    usernameLabel.grid(row=0, column=0, pady=10)

    usernameEntry = Entry(frame, width=30)
    usernameEntry.grid(row=0, column=1, pady=10, padx=20)

    passwordLabel = Label(frame, text="Enter Password", width=20, bg=color, font=("Comic Sans MS", 12, "bold"))
    passwordLabel.grid(row=1, column=0, pady=10)

    passwordEntry = Entry(frame,show="*", width=30)
    passwordEntry.grid(row=1, column=1, pady=10)

    def auth():
        import database
        usrs = database.authDetails()
        usr = usernameEntry.get()
        pas = passwordEntry.get()

        for u in usrs:
            if u == usr:
                if pas == database.getPass(usr):
                    enterPatientPage(win, frame, usr)
                    
                else:
                    messagebox.showerror('Failed', 'Wrong Password')
                break
        else:
            messagebox.showerror('Failed', 'This username doesnt exist')



    loginButton = Button(frame, text="Log In", width=20, font=("Comic Sans MS", 12, "bold"), command= auth)
    loginButton.grid(row=2 ,column=0, pady=10, columnspan=2)

    signLabel = Label(frame, text="Dont Have an Account?", width=44, bg=color)
    signLabel.grid(row=3, column=0, pady=10, columnspan=2)

    signButton = Button(frame, text='Create Account', width=20, font=("Comic Sans MS", 12, "bold"), command=lambda: signup(win, frame))
    signButton.grid(row=4, column=0, pady=10, columnspan=2)

def signup_usernamePass(win, frame, n1, d1, p1, a1, e1, t):
    n = n1.get()
    d = d1.get_date()
    p = p1.get()
    a = a1.get()
    e = e1.get()

    if n=='' or d == '' or p == '' or a == '':
        messagebox.showerror("Fill Details", "Fill all the fields")
            
    else:
        for child in frame.winfo_children():
            child.destroy()
        
        userPFrame = LabelFrame(frame, text="Create Username", bg= color)
        userPFrame.grid(row=0, column=0, padx=10, pady=10)

        username_label = Label(userPFrame, text='User Name', bg= color, width=44 )
        username_label.grid(row=0, column=0)

        username_entry = Entry(userPFrame,  width=44)
        username_entry.grid(row=1, column=0, padx=5, pady=10)

        import database
        i = database.pDetails()
        usernames = database.authDetails()

        def pass_entry():
            
            newUsername = username_entry.get()

            for vals in usernames:
                if newUsername == vals:
                    messagebox.showerror("Username Exists", "Try Again, This username exists!")
                    break

            else:
                username_entry.config(state='disabled')
                username_entry.config({'background':color})
                continueButton.destroy()

                pass_label = Label(userPFrame, text='Create Password:',  bg= color, width=44 )
                pass_label.grid(row=2, column=0)

                pass_entry = Entry(userPFrame,show="*", width=44)
                pass_entry.grid(row=3, column=0, padx=5, pady=10)

                repass_label = Label(userPFrame, text='Retype Password:', bg= color, width=44 )
                repass_label.grid(row=4, column=0)

                repass_entry = Entry(userPFrame,show="*", width=44)
                repass_entry.grid(row=5, column=0, padx=5, pady=10)

                def create():
                    pas = pass_entry.get()
                    rpas = repass_entry.get()

                    if pas != rpas:
                        messagebox.showerror("Error", "Passwords Dont Match")
                    else:
                        data = {'_id':i, 'name':n, 'dob': d.strftime("%Y/%m/%d") , 'phoneNumber': p, 'address':a, 'email': e}
                        userData = {'username': newUsername, 'password': pas, 'uid':i}
                        t["uid"] = i
                        database.insertAuth(userData)
                        database.insertProf(data)
                        database.insertRec(t)
                        messagebox.showinfo("Created", "Account Created")
                        signOrLog(win, frame)

                createAccountButton = Button(userPFrame, text='Create Account', width=44, command=create)
                createAccountButton.grid(row=6, column=0, padx=5,pady=10)

        continueButton = Button(userPFrame, text='Continue', width=44, command=pass_entry)
        continueButton.grid(row=2, column=0, pady=10, padx=5)


def signup(win, frame):
    for child in frame.winfo_children():
        child.destroy()

    win.wm_title("Sign Up")

    def save_history():
        if var.get() == 1:
            t_dict = {'record': []}
            signup_usernamePass(win, frame, name_entry, dob_entry, phone_entry, address_entry, email_entry ,t_dict)

        else:
            t=[]
            for child in signLFrame1.winfo_children():
                if isinstance(child, Text):
                    t.append(child.get("1.0",'end-1c'))
            rec_num = int(len(t)/3)
            t_rec=[]
            index = 0
            t_dict = {}

            for r in range(rec_num):
                t_rec.append([t[index], t[index+1], t[index+2]])
                index +=3
            
            t_dict['record'] = t_rec                     

            signup_usernamePass(win, frame, name_entry, dob_entry, phone_entry, address_entry, email_entry,t_dict)


    signLFrame = LabelFrame(frame, text="Personal Details", bg= color)
    signLFrame.grid(row=0, column=0, padx=10, pady=10)

    next_button = Button(frame, text='Next', width=12, font=("Comic Sans MS", 10, "bold"), command=save_history)
    next_button.grid(row=0, column=1, padx=5)

    login_butoon = Button(frame, text='Login Instead', width=12, font=("Comic Sans MS", 10, "bold"), command=lambda :login(win, frame))
    login_butoon.grid(row=0, column=2, padx=5)
    
    signLFrame1 = LabelFrame(frame, text="Medical History", bg= color)
    signLFrame1.grid(row=1, column=0, padx=9, pady=10)

    style = ttk.Style(signLFrame)
    style.theme_use('clam')
    style.configure('my.DateEntry', fieldbackground=color)
    
    name_label = Label(signLFrame, text='Patient Name', bg= color )
    name_label.grid(row=0, column=0)

    name_entry = Entry(signLFrame, bg=color, width=44)
    name_entry.grid(row=0, column=1, padx=20, pady=10)

    dob_label = Label(signLFrame, text='Date of Birth', bg= color )
    dob_label.grid(row=1, column=0, padx=40)

    dob_entry = DateEntry(signLFrame,selectmode='day', date_pattern='yyyy-MM-dd',  maxdate=today, bg=color, width=42, style='my.DateEntry')
    dob_entry.grid(row=1, column=1, padx=25, pady=10)

    phone_label = Label(signLFrame, text='Phone Number', bg= color )
    phone_label.grid(row=2, column=0)

    phone_entry = Entry(signLFrame, bg=color, width=44)
    phone_entry.grid(row=2, column=1, padx=25, pady=10)

    address_label = Label(signLFrame, text='Address', bg= color )
    address_label.grid(row=3, column=0)

    address_entry = Entry(signLFrame, bg=color, width=44)
    address_entry.grid(row=3, column=1, padx=20, pady=10)

    email_label = Label(signLFrame, text='Email', bg= color )
    email_label.grid(row=4, column=0)

    email_entry = Entry(signLFrame, bg=color, width=44)
    email_entry.grid(row=4, column=1, padx=20, pady=10)

    med_det_label = Label(signLFrame1, text="Details of Illness",  bg= color, wraplength=137, padx=5, width=17)
    med_det_label.grid(row=1, column=0)

    duration_label = Label(signLFrame1, text="Duration of Illness (Mention the years as well)",  bg= color, wraplength=137, padx=5, width=17)
    duration_label.grid(row=1, column=1)

    status_label = Label(signLFrame1, text="Status (Under Medication or Cured)",  bg= color, wraplength=137, padx=5, width=17)
    status_label.grid(row=1, column=2)

    medText = Text(signLFrame1, width=10, height=2)
    medText.grid(row=2, column=0, pady=4)

    durText = Text(signLFrame1,  width=10, height=2)
    durText.grid(row=2, column=1, pady=4)

    statusText = Text(signLFrame1,  width=10, height=2)
    statusText.grid(row=2, column=2, pady=4)

    global n 
    n = 3
    def add_rec():
        global n

        nill.config(state='disabled')

        medText = Text(signLFrame1, width=10, height=2)
        medText.grid(row=n, column=0, pady=4)

        durText = Text(signLFrame1,  width=10, height=2)
        durText.grid(row=n, column=1, pady=4)

        statusText = Text(signLFrame1,  width=10, height=2)
        statusText.grid(row=n, column=2, pady=4)

        next_button.grid(row=n, column=3, padx=3)

        def remove_rec():
            global n
            medText.destroy()
            durText.destroy()
            statusText.destroy()
            rem_button.destroy()
            n -= 1
            if n==3:
                nill.config(state='normal')

        rem_button_image =ImageTk.PhotoImage(Image.open("patientPage/images/minusButton.png"))
        rem_button = Button(signLFrame1, image=rem_button_image,  bg=color)
        rem_button.image = rem_button_image
        rem_button.grid(row=n, column=4, padx=3)
        rem_button.config(command= remove_rec)

        n += 1


    next_button_image =ImageTk.PhotoImage(Image.open("patientPage/images/plusButton.png"))
    next_button = Button(signLFrame1, image=next_button_image, command=add_rec, bg=color)
    next_button.grid(row=2, column=3, padx=7)
    next_button.image = next_button_image
    
    
    def selection():
        if var.get() == 1:
            medText.config(state='disabled')
            durText.config(state='disabled')
            statusText.config(state='disabled')
            next_button['state']='disabled'
        else:
            medText.config(state='normal')
            durText.config(state='normal')
            statusText.config(state='normal')
            next_button['state']='normal'

    var = IntVar()
    nill = Checkbutton(signLFrame1, text="No History", onvalue=1, offvalue=0, variable= var, command=selection, bg=color)
    nill.grid(row=1, column=3, columnspan=2)


def signOrLog(win, frame):
    frame.destroy()

    img = Image.open("patientPage\images\patientWallpaper.jpg")
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

    win.wm_title("Patient Account")

    signOrLogFrame = LabelFrame(win, bg=color, bd=15, relief=RIDGE)
    signOrLogFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

    signButton = Button(signOrLogFrame, text="SIGN UP",  width=20, font=_font, command=lambda:signup(win, signOrLogFrame))
    signButton.grid(row=0, column=0, pady=40, padx=20)

    label = Label(signOrLogFrame, text="----OR----", bg=color)
    label.grid(row=1, column=0)

    logButton = Button(signOrLogFrame, text="LOG IN", width=20, font=_font, command=lambda: login(win, signOrLogFrame))
    logButton.grid(row=2, column=0, pady=40, padx=20)

